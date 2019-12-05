#!/usr/bin/env python

import os, os.path
import sys
from pymongo import MongoClient
from pprint import pprint
import datetime
import boto3

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://heroku_8nscphp3:3bundtii7g7pu42cll3f62reh1@ds159387.mlab.com:59387/heroku_8nscphp3")
s3 = boto3.resource('s3')
db = client.heroku_8nscphp3
scans = db.scans

#get os arguments image_directory text_directory year month journal_date vol
image_directory_str = sys.argv[1] + "images"
image_directory = os.fsencode(image_directory_str)
text_directory_str = sys.argv[1] + "/text"
text_directory = os.fsencode(text_directory_str)
noFiles = len([name for name in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, name))])
i=0
for file in os.listdir(image_directory):
    filename = os.fsdecode(file)
    i+=1

    print ("Processing " + filename + " " + str(i) + " of " + str(noFiles))
    if os.path.isfile(os.path.join(image_directory, file)):
        basename = os.path.basename(sys.argv[1]+'/'+filename)
        new_name, _ = os.path.splitext(basename)
        content = open(text_directory_str + '/' + new_name + '.txt','r').read()
        image_key = filename
        journal = {
            "content":content,
            "image_url":"https://s3.amazonaws.com/ocr-scans/" + image_key,
            "date_added":datetime.datetime.utcnow()
        }
        scans.insert(journal)
        data = open(image_directory_str + "/" + filename, 'rb')
        s3.Bucket('ocr-scans').put_object(Key=image_key, Body=data)
