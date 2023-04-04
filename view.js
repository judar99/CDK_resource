const AWS = require('aws-sdk');

AWS.config.update({ region: 'us-east-1' }); // ajusta el valor a la region donde tienes la tabla

const dynamoDBClient = new AWS.DynamoDB.DocumentClient();

async function getAllItemsFromDynamoDB(tableName) {
  let items = [];
  let lastEvaluatedKey = null;

  do {
    const scanParams = {
      TableName: tableName,
      ExclusiveStartKey: lastEvaluatedKey,
    };

    const result = await dynamoDBClient.scan(scanParams).promise();
    items = items.concat(result.Items);
    lastEvaluatedKey = result.LastEvaluatedKey;
  } while (lastEvaluatedKey != null);

  return items;
}

// ejemplo de uso
getAllItemsFromDynamoDB('NombreDeTuTabla').then(items => {
  console.log('Items:', items);
}).catch(error => {
  console.error('Error:', error);
});
