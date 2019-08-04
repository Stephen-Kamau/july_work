import sqlite3
#create the database name using connect()
db=sqlite3.connect("student_data.db")
#use cursor() object
cursor=db.cursor()
#create a table if it is not found
cursor.execute("""CREATE TABLE IF NOT EXISTS student(id integer primary key,name text not null,age integer,phone_no integer);""")

#collect the inputs from the user
nem=input("Enter the name: ")
eg=input("Enter the age: ")
phone=input("Enter the phone number: ")
#insert the data collected from the user into the table
cursor.execute("""INSERT INTO student(name,age,phone_no) VALUES(?,?,?)""",(nem,eg,phone))

db.commit()
db.close()
