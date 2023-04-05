import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambdaFuncion(event, context):
    
    table_name = 'CDK-InventoryTableFD135387-1PJCZGC6IAOMO'
    product_name = event['pathParameters']['product']
    
    try:
        response = dynamodb.scan(
            TableName=table_name,
            FilterExpression='product_name = :product_name',
            ExpressionAttributeValues={
                ':product_name': {'S': product_name}
            }
        )
        
        if response['Count'] == 0:
            return {
                'statusCode': 404,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST'
                },
                'body': json.dumps({'message': f'Product with name {product_name} not found'})
            }
        
        item = response['Items'][0]
        product_id = item['id']['S']
        
        dynamodb.delete_item(
            TableName=table_name,
            Key={
                'id': {'S': product_id}
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST'
            },
            'body': json.dumps({'message': f'Product with name {product_name} and id {product_id} deleted successfully'})
        }
    except:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST'
            },
            'body': json.dumps({'message': f'Error deleting product with name {product_name}'})
        }
