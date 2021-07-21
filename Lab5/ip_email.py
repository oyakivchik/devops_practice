import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sqlalchemy import create_engine
from ssl import create_default_context

filename = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]
receiver = sys.argv[4]
subject = 'Myroslav-Platanovkyi-341sk Lab5'

engine = create_engine('sqlite:///{}'.format(filename), echo = False)
conn = engine.connect()
ip = conn.execute("SELECT DISTINCT ip_address from access_logs")
body = 'Unique ips: \n'+', '.join(map(lambda row: row['ip_address'],ip))

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = email
message["To"] = receiver
message.attach(MIMEText(body, "plain"))

context = create_default_context()
with SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	server.login(email, password)
	server.sendmail(email, receiver, message.as_string())

conn.close()
