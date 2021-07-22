#! /usr/bin/python3

from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy import create_engine

access_logs = Table(
	'access_logs', MetaData(),
	Column('id', Integer, primary_key=True),
	Column('hostname', String),
	Column('iip_address', String)
	Column ('date_time', DateTime),
	Column ('message', String),
)

def printLogs():
	engine = create_engine('sqllite:///access_logs.db', echo=False)
	connection = engine.connect()
	logs = connection.execute(acces_logs.select())

	for log in logs:
		print(f'{log.date_time} {log.hostname} {log.message}')

printLogs()
