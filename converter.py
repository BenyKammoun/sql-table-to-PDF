import mysql.connector
from mysql.connector import errorcode

# Connection to Mysql database
config = {
    'host':'workersdemo.mysql.database.azure.com',
    'user':'myadmin@workersdemo',
    'password':'365B&563',
    'database':'quickstartdb'
}

try:
    connection = mysql.connector.connect(**config)
    print('Connected to database ...')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = connection.cursor()