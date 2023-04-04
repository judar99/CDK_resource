import boto3
from pprint import pprint
dynamodb = boto3.client('dynamodb')
import json


# Operaciones CRUD

import uuid

def create_item(note):
    item = {
        'id': {'S': str(uuid.uuid4())},
        'descripcion': {'S': note},
    }
    response = dynamodb.put_item(TableName="CDK-NoteTable0B067050-3UNMAHU8HWFV", Item=item)
    print("a")
    print(response)
    return response


create_item(note='Recordar comprar leche en el supermercado')


import json
def lambda_handler(event, context):

    print ("hello")

    http_method = event['httpMethod']
    if http_method == 'POST':
        message = 'Se realiza una petición de tipo Get'
    else:
        message = 'Tipo de petición no soportada'
    
    return {
    'statusCode': 200,
    'body': json.dumps(message)
  }



