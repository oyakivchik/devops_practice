import sys
from sqlalchemy import create_engine

engine = create_engine('sqlite:///access_logs.db', echo = False)
connection = engine.connect()

user_ip = sys.argv[1] 
que = "SELECT * FROM access_logs WHERE user_ip=:ip" 
info = connection.execute(que, ip = user_ip).fetchall()
connection.close()

for d in info:
 print(d)
