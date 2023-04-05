import boto3
import json
from pprint import pprint

dynamodb = boto3.client('dynamodb')


def read_items(tablename):
    response = dynamodb.scan(TableName=tablename)
    return response['Items']

def lambdaFuncion(event, context):
    
    table_name = 'CDK-InventoryTableFD135387-1PJCZGC6IAOMO'
    items = read_items(table_name)
    result = json.dumps(items)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': result
    }

