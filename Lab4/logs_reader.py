import sys
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///parsered.db', echo = True)
connection = engine.connect()
ip_address = sys.argv[1] 

query_text = "SELECT * FROM logs WHERE ip_address = '{}'".format(ip_address) 

sql_query = text(query_text)
result = connection.execute(text)
result_as_list = result.fetchall()

connection.close()
for data in result_as_list:
	print(data)
