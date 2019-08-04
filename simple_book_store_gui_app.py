import sqlite3
from tkinter import*
#A simple book store
#it stores the title of the book,author name,,year and isbn number


#=============creation the main window=========
win=Tk()
win.title("Simple book record database:")
win.geometry('430x280')
win.resizable(height=False,width=False)

#========================here then we are going to impliment our database part using sqlite3==========
#we need to create functions for the buttons defined above


#==========create connection and creation of the table of the dtabase====
conn=sqlite3.connect("books_store.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key,title text,author text,year integer,isbn integer)")
conn.commit()
conn.close()

#=============function for inserting data =====================
def insert_data():
	conn=sqlite3.connect("books_store.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(text_title,text_author,text_year,text_isbn))
	conn.commit()
	conn.close()

#==========view function==============
def view_data():
	conn=sqlite3.connect("books_store.db")
	cur=conn.cursor()
	cur.execute("SELECT* FROM book")
	row_data=cur.fetchall()
	conn.close()
	return row_data

#===========search function======
def search_data(title="",author="",year="",isbn=""):
	conn=sqlite3.connect("books_store.db")
	cur=conn.cursor()
	cur.execute("SELECT* FROM book WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
	row_data=cur.fetchall()
	conn.close()
	return row_data

def delete_data():
	conn=sqlite3.connect("books_store.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,))
	conn.commit()

def update_data():
	conn=sqlite3.connect("books_store.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET  title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,isbn,id))
	conn.commit()
	conn.close()


#===========creation of labels for the entries=======
l1=Label(win,text='Title:')
l1.grid(row=0,column=0)
l2=Label(win,text='Author:')
l2.grid(row=0,column=2)
l3=Label(win,text='Year:')
l3.grid(row=1,column=0)
l4=Label(win,text='ISBN:')
l4.grid(row=1,column=2)


#=============variables definitions for the entry===========
text_title=StringVar()
text_author=StringVar()
text_year=StringVar()
text_isbn=StringVar()

#===================creation of entries places for data=============
en1=Entry(win,textvariable=text_title)
en1.grid(row=0,column=1)
en2=Entry(win,textvariable=text_author)
en2.grid(row=0,column=3)
en3=Entry(win,textvariable=text_year)
en3.grid(row=1,column=1)
en4=Entry(win,textvariable=text_isbn)
en4.grid(row=1,column=3)

#===========definition of the list box============
list1=Listbox(win,height=10,width=40)
list1.grid(row=2,column=0,columnspan=2,rowspan=6)

#addind a scrollbar to the listbox
scroll=Scrollbar(win)
scroll.grid(row=2,column=2,rowspan=6)


#=============definition of the database button=============
#these buttons include...view all,search entry,,update an entry,,delete an entry,add an entry
#View all entry 
view_btn=Button(win,text='View All',command=view_data)
view_btn.grid(row=2,column=3)

#search entries
search_btn=Button(win,text='Search Entry',command=search_data)
search_btn.grid(row=3,column=3)

#add entries
add_btn=Button(win,text='Add Entry',command=insert_data)
add_btn.grid(row=4,column=3)

#update entry
update_btn=Button(win,text='Update Selected',command=update_data)
update_btn.grid(row=5,column=3)

#delete entry
del_btn=Button(win,text='Delete Selected',command=delete_data)
del_btn.grid(row=6,column=3)

#close the datbase
close_btn=Button(win,text='Close',command=win.quit())
close_btn.grid(row=7,column=3)







win.mainloop()