from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('todo')

created_time = 12345
title = "We are doing a test"

response = table.update_item(
    Key={
        'created_time': created_time,
        'title': title
    },
    UpdateExpression="set assignee = :a, deadline=:d",
    ExpressionAttributeValues={
        ':a': "Ddrew",
        ':d': "Now."
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))