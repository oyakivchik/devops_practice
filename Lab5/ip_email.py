# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#creating_engine
engine = create_engine('sqlite:///access.db', echo=False)
meta = MetaData()

#defining table "access_logs"
access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

print('Loading...')
#connect to database
conn = engine.connect()

#selec all uniqe ip addresses from column "ip_address" form table "access_logs"
sel = select(access_logs.c.ip_address).distinct()
# sel = select(access_logs)

#select all data from database
result = conn.execute(sel)

res_list = ''
print('\n')
for row in result:
    res_list += '<li><i><b>'+row.ip_address+'</b></i></li>\n'
    print(row.ip_address)

#closing the connection
conn.close()
print('Done')

sender_email = "tsarik197566@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Ivan-Tsaryk-341sk Lab5"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text of your message
text = """\
Hi"""

# Turn these into plain MIMEText objects
part1 = MIMEText(text, "plain")

# Add plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)

print('Sending email...')
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Done')