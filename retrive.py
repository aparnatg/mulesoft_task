import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Viguuammuss",
  database="student"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM stud")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
