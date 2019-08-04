import sqlite3
from tkinter import*

def add_to_list():
	new_name=sname.get()
	new_grade=sgrade.get()
	cursor.execute("""
	        INSERT INTO scores(
	        name,score
	        )
	        VALUES(?,?)
		    """,(new_name,new_grade))

	




def clear_list():
	sname.delete()
	sgrade.delete()
	sname.focus()


db=sqlite3.connect("test_scores.db")
cursor=db.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS
	scores(ID integer primary key,name text,score integer);""")

window=Tk()
window.title("Test Scores table")
window.geometry('450x500')

label_1=Label(text='Enter the Student\'s name: ')
label_1.place(x=30,y=35)
sname=Entry(text="")
sname.place(x=150,y=35,width=200,height=25)
sname.focus()


label_2=Label(text='Enter the Student\'s scores: ')
label_2.place(x=30,y=80)
sgrade=Entry(text="")
sgrade.place(x=150,y=80,width=200,height=25)
sgrade.focus()

add_btn=Button(text='Add',command=add_to_list)
add_btn.place(x=150,y=120,width=75,height=25)


clear_btn=Button(text='Add',command=clear_list)
clear_btn.place(x=250,y=120,width=75,height=25)


window.mainloop()
db.close()