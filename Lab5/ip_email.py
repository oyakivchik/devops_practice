import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import *
from sqlalchemy.sql import select

engine = create_engine('sqlite:///access.db', echo=False)

connectionstring = engine.connect()
query = "select distinct ip_address from access_logs" 
result = connectionstring.execute(query)
result_list = []

for row in result:
    result_list += str(row.ip_address)+'\n'
    print(row.ip_address)

connectionstring.close()


sender_email = "jekas3npai@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"
password = "258456123456789j"

message = MIMEMultipart("alternative")
message["Subject"] = "Євгеній-Іващенко-СН-31 Lab5"
message["From"] = sender_email
message["To"] = receiver_email

text = result_list
mess = MIMEText(text, "plain")
message.attach(mess)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Exiting...")
