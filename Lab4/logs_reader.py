#! /usr/bin/python3

from db_tables import access_logs
from sqlalchemy import create_engine


def printLogs():
    engine = create_engine('sqlite:///access_logs.db', echo=False)
    connection = engine.connect()
    logs = connection.execute(access_logs.select())

    for log in logs:
        print(f'{log.date_time} {log.hostname} {log.message}')


printLogs()
