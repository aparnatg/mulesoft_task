from flask import Flask
app = Flask(__name__)
@app.route('/insert')
def insert():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Viguuammuss",
      database="student"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO stud (name, address) VALUES (%s, %s)"
    val = val = [
      ('Vivek', 'Lissy'),
      ('Aaradhya', 'Thoppumpady'),
      ('Hari', 'Malayatoor'),
      ('Maya', 'Vazhakala'),
      ('Sneha', 'Ottapalam'),
      ('Bincy', 'Gandhinagar'),
      ('Rishi', 'Kadavantara'),
      ('Susan', 'Kakkanad'),
      ('Vicky', 'Thevara'),
      ('Ben', 'Pullepady'),
      ('Vincent', 'Cheranaloor'),
      ('Cycy', 'Mulanthuruthy'),
      ('Vimala', 'Angamaly')
    ]
    mycursor.executemany(sql, val)

    mydb.commit()

    return print(mycursor.rowcount, "was inserted.")

@app.route('/retrive')
def retrive() :
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
                 return x
if __name__=="__main__" :
    app.run(debug=True)
