import requests
import json
import pymysql


# gets JSON data using API url and REST
response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")

# stores JSON data
response_json = response.json()

# sets up a connection to local mysql server using pymysql lib
con = pymysql.connect(host="localhost", user="root",password="pw", db="json")
cursor = con.cursor()

for key in response_json:
   userID = key['userId']
   id = key['id']
   title = key['title']
   completed = key['completed']

   cursor.execute("INSERT INTO json_mysql(userID, id, title, completed) VALUES (%s, %s, %s, %s)", (userID, id, title, completed))

con.commit()
con.close()
