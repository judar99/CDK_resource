import json
import boto3
import json
from pprint import pprint

dynamodb = boto3.client('dynamodb')


def create_item(tablename, id_product, product, images):
    response = dynamodb.put_item(
        TableName=tablename,
        Item={
            'id': {'S': id_product},
            'product': {'S': product},
            'images': {'S': images}
        }
    )
    return response

def lambdaFuncion(event, context):
    
    try:
    
        body = json.loads(event['body'])
        product_id = body['id']
        product = body['product']
        images = body['images']
    
        table_name = 'CDK-InventoryTableFD135387-1PJCZGC6IAOMO'
        create_item(table_name, product_id, product, images)
    
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE ,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Api-Key,X-Amz-Security-Token'
    
            },
            'body': json.dumps({
                
                "messege":"Item created successfully"
                
            })
        }
    except Exception as e :
        
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE ,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Api-Key,X-Amz-Security-Token'
    
            },
            'body': json.dumps({
                
                "messege":str(e)
                
            })
        }
