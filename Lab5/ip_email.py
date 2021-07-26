#! /usr/bin/python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sqlalchemy import create_engine
from ssl import create_default_context
from sys import argv


def getFilePath():
    if argv[1:]:
        return argv[1]
    else:
        print('No path to db file received')
        exit()


def getUniqueIp():
    engine = create_engine(f'sqlite:///{getFilePath()}', echo=False)
    connection = engine.connect()

    ip_list = connection.execute('SELECT DISTINCT ip_address FROM access_logs')
    return list(ip_list)


def sendToEmail(data):
    if argv[2:] and argv[3:] and argv[4:]:
        login = argv[2]
        password = argv[3]
        receiver = argv[4]
        subject = 'Волощук-Нікіта-325ск Lab5'
        body = 'Unique ip addresses list\n' + '\n'.join(map(lambda row: row['ip_address'], data))

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = login
        message["To"] = receiver
        message.attach(MIMEText(body, "plain"))

        context = create_default_context()
        with SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(login, password)
            server.sendmail(login, receiver, message.as_string())
        print('Data was successfully sent to email')

    else:
        print('There are no sender login and password, receivers addresses list in params')
    return


ips = getUniqueIp()

if len(ips):
    sendToEmail(ips)
else:
    print('There are no data in db')
