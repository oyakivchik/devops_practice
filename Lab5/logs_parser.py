import sys
import re
import time
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

#Creating engine
engine = create_engine('sqlite:///access_logs.db', echo = False)

#Creating table 'access_logs'
meta = MetaData()
access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
meta.create_all(engine)

#Connecting to database
connection = engine.connect()
logs = []

#Open file for reading
file = open(sys.argv[1], 'r')

print("Processing... Please wait...")

#Processing all the lines in file
for line in file:
    string = re.compile(r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$').search(line)
    if string:
        datetime_str = string.group(1) + " " + str(datetime.now().year)
        datetime_obj = datetime.strptime(datetime_str, '%b %d %H:%M:%S %Y')
        logs.append({
            "hostname": string.group(3), 
            "ip_address": string.group(6),
            "date_time": datetime_obj,
            "message": string.group(5)
        })

#Pushing data to database
relust = connection.execute(access_logs.insert(None), logs)
print('Finished')

#Closing file and connection
file.close()
connection.close()







