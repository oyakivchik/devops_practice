import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sqlalchemy import create_engine
from credentials import email, password

receiver = sys.argv[1]
subject = 'Ali-Hassan-343 Lab5'

engine = create_engine('sqlite:///{}'.format('access_logs.db'), echo = False)
connection = engine.connect()
ips = connection.execute('SELECT DISTINCT ip_address from access_logs')

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
