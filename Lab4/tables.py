from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

access_logs = Table(
    'access_logs', MetaData(),
    Column('id', Integer, primary_key=True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
