import sys
from sqlalchemy import create_engine

engine = create_engine('sqlite:///access_logs.db', echo = False)
con = engine.connect()
ip = sys.argv[1]
logs = con.execute(ip).fetchall()
con.close()

for c in logs:
    print(c)
