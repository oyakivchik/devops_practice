#! /usr/bin/env python3

#витягувати з БД унікальні адреси, з яких відбувалися спроби взаємодіяти з SSH сервером, і відправляти цей список електронною поштою на скриньку olexiy.jakivtchik@gmail.com

import os, smtplib
from sqlalchemy import create_engine
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ssl import create_default_context

#Get arguments from system vars
sender_email = os.environ['SENDER_EMAIL']
receiver_email = os.environ['RECEIVER_EMAIL']
email_password = os.environ['EMAIL_PASSWORD']
smtp_server = os.environ['SMTP_SERVER']
smtp_port = int(os.environ['SMTP_PORT'])

print(sender_email)
print(receiver_email)
print(email_password)
print(smtp_server)
print(smtp_port)

subject = "Катерина-Вознюк-343 Lab5"


#Connecting to database
engine = create_engine('sqlite:///access_logs.db', echo = False)

#Connect to engine
connection = engine.connect()


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Create the text of your message
ips = connection.execute('SELECT DISTINCT ip_address from access_logs')
text = 'Unique ips: \n' + '\n '.join(map(lambda row: row['ip_address'],ips))
text = MIMEText(text, "plain")

# Add plain-text part to MIMEMultipart message
message.attach(text)

#Convert message to string
text = message.as_string()

print(text)

# Create secure connection with server and send email
context = create_default_context()
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    server.login(sender_email, email_password)
    server.sendmail(sender_email, receiver_email, text)

connection.close()
