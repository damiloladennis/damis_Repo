import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event,context):
    bucket_list = []
    for bucket in s3.bucket_list.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    return {
        'statusCode' : 200,
        'Body': bucket_list
    }
