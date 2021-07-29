#! /usr/bin/env python3

#буде обробляти записи журналу подій SSH-сервера і результати записувати у базу даних за допомогою SQLAlchemy

#Importing
import re
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import argparse
from re import compile
from datetime import datetime

#Get path of file from agruments
parser=argparse.ArgumentParser(
	description="Get path of file to be parsed"
)

parser.add_argument(
	"src",
	help="input path of file to be parsed",
	type=str,
)

args=parser.parse_args()



#Connecting to database
engine = create_engine('sqlite:///access_logs.db', echo = False)

#Creating table:
meta = MetaData()

access_logs = Table('access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)

meta.create_all(engine)

#Connect to engine
conn = engine.connect()

# Insert some value
logs_entries = [] #list with dicts

#Set source of file to be parsed
src = args.src

#Get file from path given in arguments
file = open(src, 'r')

#Parse file
for line in file:
	entry = compile(
		r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s'+
		'+\d{1,2}'+'\s'+
		'+\d{2}:\d{2}:\d{2})'+'\s'+
		'+(\S+)'+'\s'
		'+(sshd)\S+:\s'+
		'+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$').search(line)
	if entry:
        	datetime_str = entry.group(1) + " " + str(datetime.now().year)
        	datetime_obj = datetime.strptime(
			datetime_str, '%b %d %H:%M:%S %Y'
		)
        	logs_entries.append({
    			"hostname": entry.group(3),
    			"ip_address": entry.group(6),
    			"date_time": datetime_obj,
    			"message":entry.group(5)
  		})

df = pd.DataFrame(logs_entries)
df.to_excel("access_logs.xlsx")

#Bulk insert:
result = conn.execute(access_logs.insert(None), logs_entries)
file.close()

#Connection close
conn.close()
