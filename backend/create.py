import json
import boto3
import uuid
import cgi
import base64
from io import BytesIO


s3_client = boto3.client('s3')

def lambdaFuncion(event, context):
    
    try:
        
        body = json.loads(event['body'])
        amount = body['amount']
        product  = body ['product']
        base64_image = body['base64Image']
        
        image = BytesIO(base64.b64decode(base64_image))

       
        file_name = str(uuid.uuid4()) + '.png'
      
        image_url = 'https://cdk-imgbucketa8fcdd83-104wrly1ypfyx.s3.amazonaws.com/' + file_name
        
        s3_client.put_object(
            Body=image,
            Bucket='cdk-imgbucketa8fcdd83-104wrly1ypfyx',
            Key=file_name,
            ACL='public-read',
            ContentType='image/png'
        )
        
        # Agregar el registro de imagen en DynamoDB
        dynamodb = boto3.client('dynamodb')
        item_id = str(uuid.uuid4())
        image_url = 'https://cdk-imgbucketa8fcdd83-104wrly1ypfyx.s3.amazonaws.com/' + file_name
        
        dynamodb.put_item(
            TableName='CDK-InventoryTableFD135387-1PJCZGC6IAOMO',
            Item={
                'id': {'S': item_id},
                'product': {'S': product},
                'amount': {'S': amount},
                'images': {'S': image_url}
            }
        )
      
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE ,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Api-Key,X-Amz-Security-Token'
            },
            'body': json.dumps({
                'message': 'File uploaded successfully',
                'url': image_url
                
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
                'message': 'Error uploading file: ' + str(e),
                
            })
        }
