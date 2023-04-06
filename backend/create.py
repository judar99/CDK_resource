def create_item(tablename, id, product, images):
    response = dynamodb.put_item(
        TableName=tablename,
        Item={
            'id': {'S': id},
            'product': {'S': product},
            'images': {'S': images}
        }
    )
    return response

def lambdaFuncion(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        id = body['id']
        product = body['product']
        images = body['images']

        table_name = 'CDK-InventoryTableFD135387-1PJCZGC6IAOMO'
        create_item(table_name, id, product, images)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': 'Item created successfully'
        }
    else:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': 'Invalid request'
        }
