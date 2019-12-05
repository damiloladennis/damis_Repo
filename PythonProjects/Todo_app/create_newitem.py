from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('todo')

created_time = 54321
title = "We another test"
task = "Inserting newer items"
deadline = "now"
assignee = "Sally"

response = table.put_item(
   Item={
        'created_time': created_time,
        'title': title,
        'task': task,
        'deadline': deadline,
        'assignee': assignee,
   }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))