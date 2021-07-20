import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text, select

engine = create_engine('sqlite:///access_logs.db', echo = False)
#create table
meta=MetaData()
access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
print("Reading... Please wait...")
sql_req = text("SELECT * FROM access_logs")
i=0
connection = engine.connect()
result = connection.execute(sql_req).fetchall()
connection.close()
for element in result:
    i=i+1
    print(element)

print("Finished")
