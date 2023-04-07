import json
import boto3
dynamodb = boto3.resource('dynamodb')

def delete_item(tablename, id_product):
    table = dynamodb.Table(tablename)
    response = table.delete_item(
        Key={
            'id': id_product
        }
    )
    return response

def lambdaFuncion(event, context):
    try:
        body = json.loads(event['body'])
        product_id = body['id']
        table_name = 'CDK-InventoryTableFD135387-1PJCZGC6IAOMO'
        delete_item(table_name, product_id)
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE ,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Api-Key,X-Amz-Security-Token'
            },
            'body': json.dumps({
                "messege":"Item deleted successfully"
            })
        }
    except Exception as e:
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
