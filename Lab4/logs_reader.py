#! /usr/bin/env python3

#Він повинен приймати в якості аргументу командного рядка ip-адресу і виводити інформацію про всі події, пов’язані з цією ip-адресою

import argparse
from sqlalchemy import create_engine

#Get ip_address from agruments
parser=argparse.ArgumentParser(
	description="Get ip address from database to be searched"
)

parser.add_argument(
	"ip",
	help="input ip to search in database of access logs. For example, 112.133.246.93",
	type=str,
)

args=parser.parse_args()


#Set ip_address to be parsed
ip_address = args.ip

#Connecting to database
engine = create_engine('sqlite:///access_logs.db', echo = False)

#Connect to engine
connection = engine.connect()

#Selecting rows with current ip_address
text = "SELECT * FROM access_logs WHERE ip_address=:ip" 
result = connection.execute(text, ip = ip_address).fetchall()
connection.close()

for data in result:
	print(data)
