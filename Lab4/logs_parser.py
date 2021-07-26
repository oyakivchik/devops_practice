from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import datetime
import re
import sys

engine = create_engine('sqlite:///access.db', echo=False)
meta = MetaData()

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
file = open(sys.argv[1],'r') 

for lines in file:
    line = re.findall('^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$',line)
    if line:
        print(line)
        print('\n0 Date:',line[0][0])
        print('\n1 Month:',line[0][1])
        print('\n2 Something:',line[0][2])
        print('\n3 Hostname:',line[0][3])
        print('\n4 Message:',line[0][4])
        print('\n5 Ip address:',line[0][5])
        ins = access_logs.insert().values(
            hostname= line[0][3],
            ip_address= line[0][5],
            message= line[0][4])

file.close()
result = connection.execute(ins)
connection.close()
