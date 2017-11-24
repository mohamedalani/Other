from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import csv, sqlite3
from dateutil.parser import parse
import re
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Path to where the csv is
path = "../../data/"

#reading csv
df = pd.read_csv(path+"emails_clean.csv")

#Creating the database
con = sqlite3.connect("test.sqlite")
db_connect = create_engine('sqlite:///test.sqlite')
try:
    df.to_sql("emails_clean", db_connect,  if_exists='append', index=False)
except: 
    pass

#Creating the API
app = Flask(__name__)
api = Api(app)
 
#Filter by sender Address
class sender(Resource):
    def get(self, sender_mail):
        if not re.match("[^@]+@[^@]+\.[^@]+", sender_mail):
            return("Not a valid email address. Please try again.")
        
        conn = db_connect.connect() # connect to database
        query = conn.execute("select date, time, sender, receiver, subject, content from emails_clean where sender = '%s' " %sender_mail  ) # This line performs query and returns json result
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if len(result) == 0:
            return({"error" : "No mails found"})
        return jsonify({'mails found': result})

#Filter by Recipient Addresses
class recipient(Resource):
    def get(self, recipient_mails):
        conn = db_connect.connect() # connect to database
        result = {}
        mails = recipient_mails.split(",")
		
		#Checking if it has a email syntax
        for mail in mails:
            if not re.match("[^@]+@[^@]+\.[^@]+", mail):
                return("Not a valid email address. Please try again : xx@xx.xx, xx@xx.xx")
          
        for mail in mails:
            query = conn.execute("select date, time, sender, receiver, subject, content from emails_clean where receiver LIKE '%"+mail+"%'") # This line performs query and returns json result
            result[mail] = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if all(v == [] for v in result.values()):
            return({"error" : "No mails found"})
			
        return jsonify({"mails found" : result})

#Filter by date range
class date_range(Resource):
    def get(self, range_):
        conn = db_connect.connect() # connect to database
        dates = range_.split(",")
        
        #Check if we have 2 dates 
        if len(dates) != 2:
            return("not a valid date interval, please enter a valid date interval : yyyy-mm-dd,yyyy-mm-dd")
        
        #Check if a valid date format
        for date in dates:
            try:
                parse(date)
            except: 
                return("not a valid date interval, please enter a valid date interval : yyyy-mm-dd,yyyy-mm-dd")
        
        query = conn.execute("select date, time, sender, receiver, subject, content from emails_clean where date BETWEEN '"+dates[0]+"' and '"+dates[1]+"'") # This line performs query and returns json result
		
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        if len(result) == 0:
            return ({"error" : "No mails found"})
        return jsonify({"mails found" : result})

#Adding routes
api.add_resource(sender, '/sender/<sender_mail>') # Route_1
api.add_resource(recipient, '/recipient/<recipient_mails>') # Route_2
api.add_resource(date_range, '/date_range/<range_>') # Route_2



if __name__ == '__main__':
     app.run(port='5002')
print("Example:")
print("http://127.0.0.1:5002/sender/phillip.allen@enron.com")
print("http://127.0.0.1:5002/recipient/tim.belden@enron.com,john.lavorato@enron.com")
print("http://127.0.0.1:5002/date_range/2000-01-01,2000-01-02")