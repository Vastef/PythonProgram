import mysql.connector

ID = input("UserID: ")
FirstName = input("FirstName: ")
LastName = input("LastName: ")
Email = input("Email: ")

mysql_connect = mysql.connector.connect(
    host="localhost",
    user="python",
    password="asdasd",
    database="pythonProgram"

)

mycursor = mysql_connect.cursor()

sql = "insert into Clients (ID, FirstName, LastName, Email) values (%s, %s, %s, %s)"
values = (ID, FirstName, LastName, Email)
mycursor.execute(sql, values)

mysql_connect.commit()

print(mycursor.rowcount, "Values have been Inserted")