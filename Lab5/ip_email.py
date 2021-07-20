import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, text, select

sender_email = "attackontitan.keshr@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Кордон-Вадим-344 Lab5"
message["From"] = sender_email
message["To"] = receiver_email

Sqlengine = create_engine('sqlite:///access_logs.db', echo = False)
#create table
meta=MetaData()
access_logs = Table(
    'access_logs', meta,
    Column('id', Integer, primary_key = True),
    Column('hostname', String),
    Column('ip_address', String),
    Column('date_time', DateTime),
    Column('message', String),
)
ip_addresses=""
print("Selecting... Please wait")
sql_req = text("SELECT Distinct ip_address FROM access_logs")
i=0
connection = Sqlengine.connect()
result = connection.execute(sql_req).fetchall()
connection.close()
for element in result:
    ip_addresses=ip_addresses+"\n"+str(element)[2:][:-3]
    
part1 = MIMEText(ip_addresses, "plain")

message.attach(part1)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )