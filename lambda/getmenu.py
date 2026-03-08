import json
import pymysql

def lambda_handler(event, context):

    connection = pymysql.connect(
        host="AWS_database_host_endpoint",
        user="user_name",
        password="db_password",
        database="foodapp"
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM menu")

    rows = cursor.fetchall()

    menu=[]

    for row in rows:
        menu.append({
        "id":row[0],
        "food_name":row[1],
        "price":row[2],
        "image_url":row[3]
        })

    return {
        'statusCode':200,
        'body':json.dumps(menu),
        'headers':{
        "Access-Control-Allow-Origin":"*"
        }
    }
