import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select

print(len(sys.argv))
if len(sys.argv) == 1:
    search_ip_address = 'all'
else:
    search_ip_address = sys.argv[1]

engine = create_engine('sqlite:///database.db', echo=False)
meta = MetaData()

access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

connection = engine.connect()

if search_ip_address == 'all':
    selecting = select(access_logs)
else:
    selecting = select(access_logs).where(access_logs.c.ip_address == search_ip_address)

result = connection.execute(selecting)

print('\n')
for row in result:
    print('Number of record:',row.id, '\nHostname:',row.hostname, '\nIp address:',row.ip_address, '\nDate/time:',row.date_time, '\nMessage: "',row.message,'"\n')

connection.close()
