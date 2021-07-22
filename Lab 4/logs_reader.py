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


request = text("SELECT * FROM access_logs")

connection = engine.connect()
result = connection.execute(request).fetchall()
connection.close()

for element in result:
    print(element)

print("Finishe")
