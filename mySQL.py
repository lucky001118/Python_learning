import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lucky@server2002"
)

#print("The data base is connected successfully. And object is: ",mydb)

mycursor = mydb.cursor()

#To check how much the databases are present in the our database management system.
print("The all database are: ")
mydatabase = []
mycursor.execute("show databases")
for x in mycursor:
    mydatabase.append(x)
print(mydatabase)

#for the showing all the tables in the target data-base
myTables = []
mycursor.execute("use usingpythondatabase")
#mydb.commit()
mycursor.execute("Show tables")
for x in mycursor:
    myTables.append(x)
print("My tables in the database is: ",myTables)

#for fatching all values in the table
mycursor.execute("Select * from customers")
myValues = mycursor.fetchall()
print("The Table values are: ")
for x in myValues:
    print(x)
#print("The table values are: ",myValues) 

#only fatch one row from the database
mycursor.execute("SELECT * from customers")
myResult = mycursor.fetchone()
print("The first tuple in the customer is: ",myResult)

#for the insertion into the customer table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")