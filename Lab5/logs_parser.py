  
from sqlalchemy import *
import argparse
import re
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--logfile", help="Enter path to file with log:", required=True)


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
resultlist = []

args = parser.parse_args()
file = open(args.logfile, 'r')

for row in file:
    line = re.compile(r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$').search(row)
    if line:
        datetime1 = line.group(1) + " " + str(datetime.datetime.now().year)
        datetime2 = datetime.datetime.strptime(datetime1, '%b %d %H:%M:%S %Y')
        resultlist.append({"hostname": line.group(3), "ip_address": line.group(6), "date_time": datetime_obj, "message":line.group(5)})
        print(line)

result = conn.execute(access_logs.insert(None), logs_entries)
file.close()
conn.close()
