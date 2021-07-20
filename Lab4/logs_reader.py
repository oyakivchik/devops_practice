import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text, select

#Creating engine
engine = create_engine('sqlite:///access_logs.db', echo = False)

#Creating table
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

#SQL request
request = text("SELECT * FROM access_logs")

#Connecting to database and making a request
connection = engine.connect()
result = connection.execute(request).fetchall()
connection.close()

#Printing all the elements
for element in result:
    print(element)

print("Finished")
