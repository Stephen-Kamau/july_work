#regestration form

from tkinter import*
import sqlite3

window=Tk()
window.geometry("500x500")
window.title("regestration form:")

full_name=StringVar()
email=StringVar()
var=IntVar()
cou=StringVar()
var1=IntVar()

def database():
	name1=full_name.get()
	email1=email.get()
	gender=var.get()
	#cou=country.get()
	pro=var1.get()
	conn=sqlite3.connect("form.db")
	with conn:
		cursor=conn.cursor()
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS
			students(
            full_name TEXT not null,
            email text not null,
            gender text not null,
            country text not null,
            programing text not null
			)

			""")

		cursor.execute("""
			INSERT INTO students(
			full_name,
			email,
			gender,
			country,
			programming
			)
			VALUES(
			?,?,?,?,?
			)
			""",
		(
			name1,
			email1,
			gender,
			cou,
			pro
		))

		conn.commit()


label0=Label(window,text="Regestration Form:",width=20,font=("bold",20))
label0.place(x=90,y=53)


label1=Label(window,text="Full Name: ",width=20,font=("bold",10))
label1.place(x=80,y=130)

entry1=Entry(window,textvar=full_name)
entry1.place(x=240,y=130)

label2=Label(window,text="Email: ",width=20,font=("bold",10))
label2.place(x=63,y=180)

entry2=Entry(window,textvar=email)
entry2.place(x=240,y=180)

label3=Label(window,text="Gender: ",width=20,font=("bold",10))
label3.place(x=70,y=230)

label4=Label(window,text="Country: ",width=20,font=("bold",10))
label4.place(x=70,y=280)

Radiobutton(window,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(window,text="Female",padx=5,variable=var,value=2).place(x=290,y=230)

list1=['Kenya','Uganda','America','Ghana','Somalia','Gerammny','Brazil','Australia','Japan']

droplist=OptionMenu(window,cou,*list1)
droplist.config(width=15)
cou.set('Select your Country')
droplist.place(x=240,y=280)

label4=Label(window,text="Programming: ",width=20,font=("bold",10))
label4.place(x=85,y=330)


var2=IntVar()
Checkbutton(window,text="Python",variable=var1).place(x=235,y=330)
Checkbutton(window,text="Python",variable=var2).place(x=290,y=330)

Button(window,text="SUBMIT",width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

window.mainloop()


















