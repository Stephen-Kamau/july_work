#attributes collection for people
from tkinter import*
import sqlite3

window=Tk()
window.geometry('450x500')
window.title("Database Application using tkinter and sql")
window.configure(background="blue")


text_in=StringVar()
text_inn=StringVar()

menu=Menu(window)
window.config(menu=menu)

def need_help():
	help(sqlite3)

submenu=Menu(menu)
menu.add_cascade(label="Help",menu=submenu)
submenu.add_command(label="sqlite3 Docs",command=need_help)


db=sqlite3.connect("Mysql.db")
cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS  
	people
	(
	name text NOT NULL,
	phone_No integer NOT NULL
	)""")
db.commit()
cursor.close()


lab=Label(window,text="Name:",font=('None 15 bold'))
lab.place(x=0,y=0)

entry_name=Entry(window, font=('None 15 bold'),textvar=text_in)
entry_name.place(x=80,y=0)

phone_no=Entry(window, font=('None 15 bold'),textvar=text_in)
phone_no.place(x=80,y=40)

lab=Label(window,text="Phone:",font=('None 15 bold'))
lab.place(x=0,y=40)

def insert_data():#find the prloblem in this function
	nem=text_in.get()
	phone=text_inn.get()
	conn=sqlite3.connect("Mysql.db")
	with conn:
		cursor=conn.cursor()
		cursor.execute("""INSERT INTO
		 people
		 (
		 name,phone_No
		 ) 
		 VALUES(?,?)""",
		 (nem,phone))
	conn.commit()
	conn.close()

def show_data():
	conn2=sqlite3.connect("Mysql.db")
	cursor=conn2.cursor()
	cursor.execute(SELECT * people)
	for row in cursor.fetchall():
		print(row)


name=StringVar()
phone=StringVar()

def update_data():
	nm=name.get()
	ph=phone.get()


	conn3=sqlite3.connect("Mysql.db")
	cursor=conn3.cursor()
	cursor.execute("UPDATE people SET name= ?  WHERE phone_No= ? ",(nm,ph))
	conn3.commit()


def drop_data():
	conn4=sqlite3.connect("Mysql.db")
	cursor=conn4.cursor()
	cursor.execute("DROP table people")
	cursor.commit()

dell=StringVar()
def delete_data():
	dee=dell.get()
	conn5=sqlite3.connect("Mysql.db")
	cursor=conn5.cursor()
	cursor.execute("DELETE FROM people WHERE name=? ",(dee,))
	coonn5.commit()
	conn5.close()


button_drop=Button(window,pady=2,padx=2,text="Drop Table: ",command=drop_data,font=('None 15 bold'))
button_drop.place(x=180,y=360)

button_update=Button(window,pady=2,padx=2,text="Update: ",command=drop_data,font=('None 15 bold'))
button_update.place(x=80,y=280)

label_name=Label(window,text="Update name: ",font=('None 15 bold'))
label_name.place(x=0,y=200)


entry_to_update_name=Entry(window,width=20,font=('None 15 bold'),textvar=name)
entry_to_update_name.place(x=160,y=200)

label_phone=Label(window,text="Provide phone No: ",font=('None 15 bold'))
label_phone.place(x=0,y=240)

entry_to_update_phone=Entry(window,width=20,font=('None 15 bold'),textvar=phone)
entry_to_update_phone.place(x=210,y=240)


label_delete=Label(window,text="DELETE: ",font=('None 15 bold'))
label_delete.place(x=0,y=340)


entry_delete=Entry(window,width=20,font=('None 15 bold'),textvar=dell)
entry_delete.place(x=90,y=340)



button_delete=Button(window,pady=2,padx=2,text="Delete: ",command=delete_data,font=('None 15 bold'))
button_delete.place(x=90,y=380)


button_insert=Button(window,pady=2,padx=2,text="Submit: ",command=insert_data,font=('None 15 bold'))
button_insert.place(x=60,y=100)


button_show=Button(window,pady=2,padx=2,text="SHOW: ",command=show_data,font=('None 15 bold'))
button_show.place(x=160,y=100)


window.mainloop()





























