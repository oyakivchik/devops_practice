import sys
from sqlalchemy import create_engine

engine = create_engine('sqlite:///access_logs.db', echo = True)
connection = engine.connect()
ip_address = sys.argv[1] 

text = "SELECT * FROM access_logs WHERE ip_address=:ip" 
result = connection.execute(text, ip = ip_address).fetchall()
connection.close()
for data in result:
 print(data)
