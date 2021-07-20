from sqlalchemy import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--ip", help="Ip:", required=True)
args = parser.parse_args()
ip = args.ip
engine = create_engine('sqlite:///access_logs.db')
meta = MetaData()

access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),)

meta.create_all(engine)

conn = engine.connect()
request="select * from access_logs where ip_address="+str(ip)
result = conn.execute(request).fetchall()

for i in result:
  print(i)
conn.close()
