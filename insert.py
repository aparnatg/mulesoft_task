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

print(mycursor.rowcount, "was inserted.")
