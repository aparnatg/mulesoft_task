from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Viguuammuss",
  database="student"
)


class People(Resource):
    def get(self):
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

        return str(mycursor.rowcount) +" was inserted"

    def post(self):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM stud")

        myresult = mycursor.fetchall()
        students=[]
        for x in myresult:
            students.append(x)
        return students

api.add_resource(People,"/Data")

if __name__ == '__main__':
    app.run(debug=True)
