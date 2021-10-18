import time
from flask import Flask
import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
import json

app = Flask(__name__)

@app.route('/API')
def API():
    #Configure the below according to your mssql settings
    #'DRIVER={<mssql driver>}; SERVER=<server>; Database=<db name>; UID=<user with server admin role>; PWD=<password>'
	conx = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.8.so.1.1}; SERVER=localhost; Database=Gems; UID=admin; PWD=Sysadminroot1')
	query = 'SELECT * FROM Gems.dbo.Diamonds'

	cursor = conx.cursor()
	cursor.execute(query)
	rows = cursor.fetchall()

	data = []

	conx.close()

	#Converts pyodbc row object to serializable JSON
	for row in rows:
		#data.append([str(x) for x in row])
		data.append({ str(row[0]) : [str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]),]})
		


	json_string = json.dumps(data)

	return json_string

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/')
def get_index():
    return 'This is the index path'