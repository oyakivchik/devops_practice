# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from datetime import datetime
import re
import sys

#creating_engine
engine = create_engine('sqlite:///access.db', echo=False)
meta = MetaData()

#defining table "access_logs"
access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

#create table
meta.create_all(engine)

#connect to database
conn = engine.connect()

#opening file "access.log" for "read"
f = open(sys.argv[1],'r') #'access.log'

ins= []

print('Loading...')
#loop through all lines
for line in f:
    validation = re.compile(r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$').search(line)
    if validation:
        ins.append({
            "hostname" : validation.group(3),
            "ip_address" : validation.group(6),
            "date_time" : datetime.now(),
            "message" : validation.group(5)
            })

#closing the file "access.log"
f.close()

#inserting data to database
result = conn.execute(access_logs.insert(), ins)

#closing the connection
conn.close()
print('Done')