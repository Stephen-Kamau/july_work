import sqlite3

db=sqlite3.connect("Mysql.db")
cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS  
	people
	(
	name text NOT NULL,
	phone_No integer NOT NULL
	)""")
db.commit()

name=text_in.get()
phone_No=text_in.get()
conn=sqlite3.connect("Mysql.db")
with conn:
	cursor=conn.cursor()
	cursor.execute("""INSERT INTO
	 people
	 (
	 name,phone_No
	 ) 
	 VALUES(?,?)""",
	 (name,phone_No))
conn.commit()
conn.close()