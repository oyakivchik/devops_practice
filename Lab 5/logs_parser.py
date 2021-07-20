import re
import datetime
import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

Sqlengine = create_engine('sqlite:///access_logs.db', echo = False)
#create table
meta=MetaData()
access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
print("Parsing... Please wait")
#create connection
connection = Sqlengine.connect()
meta.create_all(Sqlengine)
logs_entries = []
#open log file
logs = open(sys.argv[1], 'r')

for i in logs:
    #operating with lines of log
    element = re.compile(r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$').search(i)
    if element:
        datetime_obj = datetime.datetime.strptime(element.group(1), '%b %d %H:%M:%S')
        logs_entries.append({"hostname": element.group(3), "ip_address": element.group(6), "date_time": datetime_obj, "message":element.group(5)})

result = connection.execute(access_logs.insert(None), logs_entries)
print("Parsing was successfull!")
logs.close()
connection.close()