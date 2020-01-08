import mysql.connector
#connect to mysql
mydb = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "REKHA15@",
    database = "kajal")
if mydb:
    print("DB connected")
else:
    print("DB not connected")
#create cursor
cursor = mydb.cursor()
ec = raw_input("enter e code : ")
en = raw_input("enter e name : ")
es = raw_input("enter e salary : ")
ed = raw_input("enter e dob : ")
ecity = raw_input("enter e city : ")
sql = "insert into empmaster values("+ec+", '"+en+"', '"+en+"', "+es+", '"+ed+"', '"+ecity+"')"
cursor.execute(sql)
mydb.commit()

if cursor.rowcount>0:
    print("data inserted")
else:
    print("data did not inserted")

#retieve all data from database
sql = "select * from empmaster"
#accessing data into cursor
cursor.execute(sql)
#fetching all rows into result
result = cursor.fetchall()
for item in result:
    print(item)
#closing connection
cursor.close()
mydb.close