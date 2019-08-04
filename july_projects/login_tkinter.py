import sqlite3
from tkinter import*
from tkinter import messagebox as ms
root=Tk()


db=sqlite3.connect('login_tkinter.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user(username text not null,password not null)")
cursor.execute("SELECT* FROM user")
db.commit()
db.close()


class details():
	def __init__(self,master):
		self.master=master
		self.username=StringVar()
		self.password=StringVar()
		self.n_username=StringVar()
		self.n_password=StringVar()
		self.widgets()
	def login(self):
		db=sqlite3.connect('login_tkinter.db')
		cursor=db.cursor()
		find_person=("SELECT* FROM user WHERE username = ? AND password = ? ")
		cursor.execute(find_person,[(self.username.get()),(self.password.get())])
		results=cursor.fetchall()
		if results:
			self.logf.pack.forget()
			self.head['text']= self.username.get()
			self.head['pady'] = 150

		else:
			ms.showerror("OPPS! ", "Username matched!")


	def new_user(self):
		db=sqlite3.connect('login_tkinter.db')
		cursor= db.cursor()
		find_person=("SELECT* FROM user WHERE username = ? AND password = ? ")
		cursor.execute(find_person,[(self.username.get()),self.password.get()])
		if cursor.fetchall():
			ms.showerror("OPPS","Username taken")

		else:
			insert="INSERT INTO user (username , password ) VALUES (? , ?)"
			cursor.execute(insert,[(self.n_username.get()), (self.n_password.get())])
			db.commit()
			ms.showerror("SUCESSFUL","Account created")
			self.logf()


	def log(self):
		self.username.set("")
		self.password.set("")
		self.crf.pack_forget()
		self.head['text']= "Login"
		self.logf.pack()

	def cr(self):
		self.n_username.set("")
		self.n_password.set("")
		self.head['text']= "Create Account"
		self.logf.pack_forget()
		self.crf.pack()

	def widgets(self): 
		self.head = Label(self.master , text ="Login" , font = ('freesansbold',35),pady=40)
		self.head.pack()

		self.logf = Frame (self.master , padx = 10 ,pady =10)
		Label(self.logf , text = 'Username:' ,font=('freesansbold',20),pady=5,padx=5).grid(sticky=W)
		Entry(self.logf ,textvariable = self.username ,bd=8,font=('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
		Label(self.logf , text = 'Password::' , font=('freesansbold',20),pady=5,padx=5).grid(sticky=W)
		Entry(self.logf ,textvariable = self.password ,bd=8,font=('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
		Button(self.logf,text="Login" ,bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.login ).grid(row=2)
		Button(self.logf,text="make new account" ,bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.cr ).grid(row=2,column=1)
		self.logf.pack()

		self.crf = Frame (self.master , padx = 10 ,pady =10)
		Label(self.crf, text = 'Username:' , font=('freesansbold',20),pady=5,padx=5).grid(sticky=W)
		Entry(self.crf ,textvariable = self.n_username ,bd=8,font=('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
		Label(self.crf , text = 'Password::' , font=('freesansbold',20),pady=5,padx=5).grid(sticky=W)
		Entry(self.crf ,textvariable = self.n_password ,bd=8,font=('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
		Button(self.crf,text="Go to Login" ,bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.log ).grid(row=2)
		Button(self.crf,text="Create Account" ,bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.new_user ).grid(row=2,column=1)
		self.crf.pack()




details(root)
root.title('login page')
root.geometry("400x350")
root.mainloop()




       

