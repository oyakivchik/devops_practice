import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import *
from sqlalchemy.sql import select

engine = create_engine('sqlite:///access_logs.db', echo=False)
meta = MetaData()
result_list = ''

access_logs = Table(
    'access_logs', meta,
    Column('id',Integer,primary_key=True),
    Column('hostname',String),
    Column('ip_address',String),
    Column('date_time',DateTime),
    Column('message',String),
)

conn = engine.connect()
query = select(access_logs.c.ip_address).distinct()
result = conn.execute(query)

for row in result:
    result_list += str(row.ip_address)+'\n'
    print(row.ip_address)

conn.close()

sender_email = "zalupa.tvoego.slona@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"
password = "12345Qwert"

message = MIMEMultipart("alternative")
message["Subject"] = "Самошкін-Гліб-341 Lab5"
message["From"] = sender_email
message["To"] = receiver_email

text = result_list
mess = MIMEText(text, "plain")
message.attach(mess)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print('Completed')
