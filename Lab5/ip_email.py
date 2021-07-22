from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import select
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

print('Loading...')
conn = engine.connect()
sel = select(access_logs.c.ip_address).distinct()
result = conn.execute(sel)

res_list = ''
print('\n')
for row in result:
    res_list += '<li><i><b>'+row.ip_address+'</b></i></li>\n'
    print(row.ip_address)

#closing the connection
conn.close()
print('Done')

sender_email = "pavlinskamasha5@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Masha-Pavlinska-341sk Lab5"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Message"""

part1 = MIMEText(text, "plain")
message.attach(part1)
print('Sending email...')

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Done')