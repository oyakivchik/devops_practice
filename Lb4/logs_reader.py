# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import sys

print(len(sys.argv))
if len(sys.argv) == 1:
    search_ip_address = 'all'
else:
    search_ip_address = sys.argv[1]


#creating_engine
engine = create_engine('sqlite:///access.db', echo=False)
meta = MetaData()

print(f'Serch logs for {search_ip_address}:')

#defining table "access_logs"
access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

#connect to database
conn = engine.connect()

#selec column "ip_address" form "access_logs" table where ip_address = serch_ip_address
# if search_ip_address:
if search_ip_address == 'all':
    sel = select(access_logs)
else:
    sel = select(access_logs).where(access_logs.c.ip_address == search_ip_address)

#select all data from database
result = conn.execute(sel)

print('\n')
for row in result:
    print('Id:',row.id,
        '\nHostname:',row.hostname,
        '\nIp address:',row.ip_address,
        '\nDate time:',row.date_time,
        '\nMessage: "',row.message,'"\n')

#closing the connection
conn.close()