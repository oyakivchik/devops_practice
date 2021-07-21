import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from sqlalchemy import create_engine
from variables import email, password

file = 'access_logs.db'
receiver = sys.argv[1]
subject = 'Mykola-Popyk-343 Lab5'

engine = create_engine('sqlite:///{}'.format(file), echo = False)
connection = engine.connect()
request = 'SELECT DISTINCT ip_address from access_logs'
ips = connection.execute(request)

body = 'Unique ips: \n' + '\n '.join(map(lambda row: row['ip_address'],ips))

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = email
message["To"] = receiver
message.attach(MIMEText(body, "plain"))

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(email, password)
session.sendmail(email, receiver, message.as_string())
session.quit()

connection.close()
