from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from sqlalchemy import create_engine

login = "aoleksandr849@gmail.com"
password = "hjvfpkbq"
receiver = 'olexiy.jakivtchik@gmail.com'
subject = 'Олександр-Вінніченко-СН-21 Lab5'

engine = create_engine('sqlite:///access_logs.db', echo=False)
connection = engine.connect()
ips = connection.execute('SELECT DISTINCT ip_address from access_logs')

body = 'Перелік ір адресів: \n' + '\n '.join(map(lambda row: row['ip_address'], ips))

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = login
message["To"] = receiver
message.attach(MIMEText(body, "plain"))

with SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.ehlo()
    server.login(login, password)
    server.sendmail(login, receiver, message.as_string())

