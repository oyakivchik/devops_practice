import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text, select

engine = create_engine('sqlite:///access_logs.db', echo = False)
meta = MetaData()
access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
sql_req = text("SELECT message FROM access_logs WHERE ip_address == '{0}'".format(sys.argv[1]))

conn = engine.connect()
result = conn.execute(sql_req).fetchall()
conn.close()
for row in result:
    print(row)