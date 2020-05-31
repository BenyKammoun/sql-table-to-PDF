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

# Retrieve workers-salaries data
cursor.execute( '''
    select _id, firstname, lastname, salarymonth, sumbefor, sumafter 
    from workers, salaries 
    where workers._id = salaries.workerid
    order by _id asc;
''')
rows = cursor.fetchall()

# HTML template
headerHtml = '''
        <table>
            <tr>
                <th>מס' אישי</th>
                <th>שם פרטי</th>
                <th>שם משפחה</th>
                <th>חודש שכר</th>
                <th>סכום לפני הסכם</th>
                <th>סכום אחרי הסכם</th>
            </tr>
            <tr>
'''
footerHtml = "</table>"
