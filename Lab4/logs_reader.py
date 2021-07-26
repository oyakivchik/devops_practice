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

meta.create_all(engine)
connection = engine.connectionect()
sel = select(access_logs)

#select all data from database
result = connection.execute(sel)

print(result)
for row in result:
    print('\nId:',row.id,
        '\nHostname:',row.hostname,
        '\nIp address:',row.ip_address,
        '\nDate time:',row.date_time,
        '\nMessage: "',row.message,'"\n\n')

connection.close()
