import json
import pymysql

def lambda_handler(event, context):

    body=json.loads(event['body'])

    user=body['user']
    food=body['food']
    quantity=body['quantity']

    connection=pymysql.connect(
    host="AWS_database_ARN",
    user="user_name",
    password="db_password",
    database="foodapp"
    )

    cursor=connection.cursor()

    query="INSERT INTO orders(user,food,quantity) VALUES(%s,%s,%s)"

    cursor.execute(query,(user,food,quantity))

    connection.commit()

    return {
    "statusCode":200,
    "body":"Order placed successfully",
    "headers":{
    "Access-Control-Allow-Origin":"*"
    }
    }
