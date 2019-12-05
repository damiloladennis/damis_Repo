from pymongo import MongoClient
from pprint import pprint
import datetime
import boto3

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://heroku_24353wrj:tq5ltjpkpib8p3nbm17jcu6084@ds155278.mlab.com:55278/heroku_24353wrj")
s3 = boto3.resource('s3')
db = client.heroku_24353wrj
journals = db.journals

journal = {
"year":"2005",
"month":"october",
"journal_date":"30",
"vol":"1",
"content":"",
"image_url":"https://s3.amazonaws.com/jee-journals/",
"date_added":datetime.datetime.utcnow()
}

#journals.insert(journal)
#print (journal_id)

data = open('1.png', 'rb')
s3.Bucket('jee-journals').put_object(Key='2005/10/1.png', Body=data)
