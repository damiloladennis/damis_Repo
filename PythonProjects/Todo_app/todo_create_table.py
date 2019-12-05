from __future__ import print_function
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='todo',
    KeySchema=[
        {
            'AttributeName': 'created_time',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        },


    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'created_time',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'task',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'deadline',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'assignee',
            'AttributeType': 'S'
        },
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'index_task',
            'KeySchema': [
                {
                    'AttributeName': 'created_time',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'task',
                    'KeyType': 'RANGE'  # Sort key
                },

            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        },
        {
            'IndexName': 'index_deadline',
            'KeySchema': [
                {
                    'AttributeName': 'created_time',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'deadline',
                    'KeyType': 'RANGE'  # Sort key
                },

            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        },
        {
            'IndexName': 'index_assignee',
            'KeySchema': [
                {
                    'AttributeName': 'created_time',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'assignee',
                    'KeyType': 'RANGE'  # Sort key
                },

            ],
            'Projection': {
                'ProjectionType': 'ALL'
            }
        }
    ],

    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)

