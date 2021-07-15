# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select

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

#connect to data base
conn = engine.connect()

#selec all form "access_logs" table
sel = select(access_logs)

#select all data from data base
result = conn.execute(sel)

print(result)
for row in result:
    print('\nId:',row.id,
        '\nHostname:',row.hostname,
        '\nIp address:',row.ip_address,
        '\nDate time:',row.date_time,
        '\nMessage: "',row.message,'"\n\n')

#closing the connection
conn.close()
