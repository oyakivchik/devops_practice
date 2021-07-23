#! /usr/bin/python3

from db_tables import access_logs
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

access_logs = Table(
    'access_logs', MetaData(),
    Column('id', Integer, primary_key=True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)


def printLogs():
    engine = create_engine('sqlite:///access_logs.db', echo=False)
    connection = engine.connect()
    logs = connection.execute(access_logs.select())

    for log in logs:
        print(f'{log.date_time} {log.hostname} {log.message}')


printLogs()
