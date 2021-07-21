#! /usr/bin/python3

from datetime import datetime
#from db_tables import access_logs
from re import compile
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table


def getFilePath():
    if argv[1:]:
        return argv[1]
    else:
        print('No path to log file received')
        exit()

access_logs = Table(
    'access_logs', MetaData(),
    Column('id', Integer, primary_key=True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)

def writeFile():
    path = getFilePath()
    file = open(path, 'r')

    engine = create_engine('sqlite:///access_logs.db', echo=False)
    access_logs.metadata.create_all(engine)
    connection = engine.connect()

    logs_entries = []
    regexp = r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\S+)\s+(sshd)\S+:\s+(.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*)$'

    for line in file:
        entry = compile(regexp).search(line)
        if entry:
            datetime_str = entry.group(1) + " " + str(datetime.now().year)
            datetime_obj = datetime.strptime(datetime_str, '%b %d %H:%M:%S %Y')
            logs_entries.append({"hostname": entry.group(3), "ip_address": entry.group(6), "date_time": datetime_obj,
                                 "message": entry.group(5)})

    connection.execute(access_logs.insert(None), logs_entries)
    connection.close()
    file.close()


writeFile()
