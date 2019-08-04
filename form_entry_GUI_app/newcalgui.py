from tkinter import*

def newcalgui(source , side):
	obj1=Frame(source, borderwidth=4 , bd=4 ,bg='powered blue')
	obj1.pack(side=side , expand=YES , fill=BOTH)
	return obj1


def btn(source , side ,text , command=None):
	obj1=Frame(source , text=text, command=command)
	obj1.pack(side=side , expand=YES , fill=BOTH)
	return obj1


class calgui(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_add('*Font','arial 20 bold')
		self.pack(expand=YES,fill=BOTH)
		self.master.title("New Gen Calculator")


		display=StringVar()

		Entry(self , relief=RAISED ,justify='right' ,bd=30 ,bg='powdered blue').pack(side=TOP,expand=YES,fill=BOTH)
	for delbut in (['CE'],['C']):
		erase=newcalgui(self,TOP)
		for char in delbut:
			button(erase , LEFT ,char , lambda obj1=display ,q=char:obj1.set('') )


	for Numbut in("756/","456*","123-","0.+"):
		Numfunction=newcalgui(self,TOP)
		for char in Numbut:
			button(Numfunction,LEFT,char ,lambda obj1=display ,q=char:obj1.set(obj1.get()+q))


	equalbtn=newcalgui(self ,TOP)
	for x in "=":
		if x == "=":
			btn=button(equalbtn,LEFT,x)
			btn.button.bind("<ButtonRelease-1>",lambda e, obj1=display:calc(obj1),'+')


	gchjgkjhj;loslohsxhsxhihsihih	else:
			btn=button(equalbtn,LEFT,x,obj1=display, s=x:obj1.get(obj1.set() + s))


	def calc(self,display):
		try:
			display.set(eval(display.get()))
		except :
			display.set("ERROR wewe")
			





if __main__=='__name__':
	app().mainloop()

