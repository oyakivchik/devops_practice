import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, select

engine = create_engine('sqlite:///access_logs.db', echo = True)
meta = MetaData()
access_logs = Table(
	'access_logs', meta,
	Column('id', Integer, primary_key = True),
	Column('hostname', String),
	Column('ip_address', String),
	Column('date_time', DateTime),
	Column('message', String),
)
conn = engine.connect()
uid = sys.argv[1]
query= "SELECT * FROM access_logs WHERE ip_address = :ip"
result = conn.execute(query, ip = uid).fetchall()

for row in result:
	print(row)

conn.close()
