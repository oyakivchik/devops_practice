import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text, select

Sqlengine = create_engine('sqlite:///access_logs.db', echo = False)
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
print("Selecting... Please wait")
sql_req = text("SELECT message FROM access_logs WHERE ip_address == '{0}'".format(sys.argv[1]))
i=0
connection = Sqlengine.connect()
result = connection.execute(sql_req).fetchall()
connection.close()
for element in result:
    i=i+1
    print(element)

print(f'There was {i} records with {sys.argv[1]} ip_address in DB.')