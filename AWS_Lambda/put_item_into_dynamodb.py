import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planets')

def lambda_handler(event,context):
    response = table.put_item(
        Item = {
            'id': 'Neptune',
            'temp': 'Very very cold'
        }
    )
    response = {
        'message' : 'Item Added'
    }
    return {
        'statusCode': 200,
        'body': response
    }