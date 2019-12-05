import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')

def lambda_handler(event, context):
    # TODO implement
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    json_file_object = s3_client.get_object(Bucket=bucket_name, Key=json_file_name)
    jsonFileReader = json_file_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    for emp in jsonDict :
        print(emp)
    #Add json data to Dynamodb Table
        table.put_item(Item =emp)