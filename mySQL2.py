import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="Lucky@server2002",
    database ="usingpythondatabase"
)

mycursor = mydb.cursor()

#insertion methods
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#many inputes insert at one time
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
       ("John", "Highway 21"),
       ("John", "Highway 21"),
       ("John", "Highway 21"),
       ("John", "Highway 21")
       ]
mycursor.executemany(sql,val)
mydb.commit()
print("Successfully inserted. and ",mycursor.rowcount," values inserted successfully")

#directally inserted in the database
mycursor.execute("Insert into customers Values ('Lucky Manikpuri','h-198/2, w-11, Anjora')")
mydb.commit()
print("Inserted successfully, ",mycursor.rowcount," rows are affected! ")

#using rowName selection
print("------------------------------------------------")
mycursor.execute("Select name,address from customers")
myResult = mycursor.fetchall()
for x in myResult:
    print(x)
print("------------------------------------------------")

#using the 'where' close selection
print("Fatch with where close: ")
mycursor.execute("Select * from customers where name='Lucky Manikpuri' ")
myResult = mycursor.fetchall()
for x in myResult:
    print(x)
print("------------------------------------------------")

#fatch the values using the custmize value
myQuery ="Select * from customers where name=%s"
values = (input("Inter the name of customer wich you want to fint the reords: ") , ) #making it tuple
mycursor.execute(myQuery,values)
print("Fatch with where close and customer choise: ")
result = mycursor.fetchall()
for x in result:
    print(x)
print("------------------------------------------------")

#For the delete any value in the database
try:
    yQuery ="Delete from customers where name='Ben'"
    mycursor.execute(myQuery)
    mydb.commit()
    print("The tuple is deleted successfully, ",mycursor.rowcount)
    
except:
    print("ERROR: not find the deleting values")
print("------------------------------------------------")
#for user inpute for the delete the values

myQuery ="Delete from customers where name=%s"
values = (input("Inter the name of customer wich you want to delete the reords: ") , ) #making it tuple
mycursor.execute(myQuery,values)
mydb.commit()
print("The tuple is deleted successfully, ",mycursor.rowcount)
print("------------------------------------------------")
