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


conn = engine.connect()


sel = select(access_logs.c.ip_address).distinct()
result = conn.execute(sel)

res_list = ''
for row in result:
    res_list += '<li><i><b>'+row.ip_address+'</b></i></li>\n'
    print(row.ip_address)


conn.close()


sender_email = "olgadmitrivna09@gmail.com"
receiver_email = "olexiy.jakivtchik@gmail.com"
password = "Olga1972"

message = MIMEMultipart("alternative")
message["Subject"] = "Lb5 GitHub Actions"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = f"""\
<html>
  <body>
    <h3>Oleksandr-Kopiievyi-344-Lab5</h3>
    <h1>Hi, hear is all ip addresses:</h1>
    <hr/>
    <ol>
        {res_list}
    </ol>
  </body>
</html>
"""


part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Done')
