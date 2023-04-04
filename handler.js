const AWS = require ('aws-sdk');
const dynamo = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = process.env.TABLE


async (event)=>{
    
    const description = event.queryStringParameters.description;
  
    const item = {
        id: description
    }

    const savedItem = await saveItem(item);

    return {
        statusCode: 200,
        body: JSON.stringify(savedItem),
    }
}

async function saveItem (item){
    const params= {
        TableName: TABLE_NAME,
        Item : item
    };

    return dynamo.put(params).promise().then(()=>{
        return item;
    });
}

exports.deleteNote = async (event) => {

    const description = event.queryStringParameters.description;
  
    
    const params = {
      TableName: TABLE_NAME,
      Key: { id: description }
     
    };
  
    try {
      await dynamo.delete(params).promise();
      return {
        statusCode: 200,
        body: JSON.stringify({message: `nota  ${description} eliminada`})
      };
    } catch (error) {
      console.log(error);
      return {
        statusCode: 500,
        body: JSON.stringify({message: `Error al intentar eliminar la nota ${description}`})
      };
    }
  };

