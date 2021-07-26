from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import sys

print(len(sys.argv))
if len(sys.argv) == 1:
    search_ip = 'all'
else:
    search_ip = sys.argv[1]


enginer = create_engine('sqlite:///result.db', echo=False)
meta = MetaData()

print(f'Serch logs for {search_ip}:')

access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

con = enginer.connect()

if search_ip == 'all':
    sel = select(access_logs)
else:
    sel = select(access_logs).where(access_logs.c.ip_address == search_ip)


result = con.execute(sel)

print('\n')
for row in result:
    print('Id:',row.id,
        '\nHostname:',row.hostname,
        '\nIp address:',row.ip_address,
        '\nDate time:',row.date_time,
        '\nMessage: "',row.message,'"\n')

con.close()
