from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import sys

print(len(sys.argv))
if len(sys.argv) == 1:
    ip_address = 'all'
else:
    ip_address = sys.argv[1]






enginer = create_engine('sqlite:///logs.db', echo=False)
meta = MetaData()


access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)





conect = enginer.connect()

if ip_address == 'all':
    sel = select(access_logs)
else:
    sel = select(access_logs).where(access_logs.c.ip_address == ip_address)


result = conect.execute(sel)



for row in result:
    print('Id:',row.id,'\nHostname:',row.hostname,'\nIp address:',row.ip_address,'\nDate time:',row.date_time,'\nMessage: "',row.message,'"\n')

conect.close()
