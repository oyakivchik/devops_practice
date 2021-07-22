from sqlalchemy import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--find", help="Enter ip you need to find:", required=True)

engine = create_engine('sqlite:///access_logs.db')
connectionstring = engine.connect()

args = parser.parse_args()
find = args.find
request= "select * from access_logs where ip_address="+str(find)

result = connectionstring.execute(request).fetchall()

for row in result:
  print(row)
connectionstring.close()
