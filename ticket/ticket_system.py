from tkinter import*
from tkinter import Tk, StringVar ,ttk ,messagebox
import random
import time;
import datetime

root=Tk()
root.geometry("1350x750+0+0")
root.title("Ticket system")
root.configure(background='black')



#>>>>>>>>>>>>>>>>>>>>>..variables.<<<<<<<<<<<<<<<<<<<<<<<
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
sub_total=StringVar()
tax=StringVar()
total=StringVar()
text_input=StringVar()
operator=""
Date1=StringVar()
time1=StringVar()
var10=StringVar()
var11=StringVar()
class1=StringVar()
ref=StringVar()
to=StringVar()
fees=StringVar()
from1=StringVar()
adult=StringVar()
child=StringVar()
price=StringVar()
route=StringVar()



#........................set the checkbox variables to null.........
var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
total.set(0)
sub_total.set(0)
tax.set(0)


Top = Frame (root,width=1350,height=100,bd=14,relief='raised')
Top.pack(side=TOP)

f1 = Frame (root,width=900,height=650,bd=8,relief='raised')
f1.pack(side=LEFT)
f2 = Frame (root,width=440,height=650,bd=8,relief='raised')
f2.pack(side=RIGHT)

frametopright = Frame (f2,width=440,height=650,bd=12,relief='raised')
frametopright.pack(side=TOP)
framebottomright = Frame (f2,width=440,height=50,bd=16,relief='raised')
framebottomright.pack(side=BOTTOM)

f1a = Frame (f1,width=1350,height=100,bd=14,relief='raised')
f1a.pack(side=TOP)
f2a = Frame (f1,width=1350,height=100,bd=14,relief='raised')
f2a.pack(side=BOTTOM)

topleft1 = Frame (f1a,width=300,height=200,bd=16,relief='raised')
topleft1.pack(side=LEFT)
topleft2 = Frame (f1a,width=300,height=200,bd=16,relief='raised')
topleft2.pack(side=RIGHT)
topleft3 = Frame (f1a,width=300,height=200,bd=16,relief='raised')
topleft3.pack(side=RIGHT)
#>>>>>>>>>>>>>>>bottom frames <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
bottomleft1 = Frame (f2a,width=450,height=450,bd=14,relief='raised')
bottomleft1.pack(side=LEFT)


bottomleft2 = Frame (f2a,width=450,height=450,bd=14,relief='raised')
bottomleft2.pack(side=RIGHT)

#>>>>>>>>>backgronds  <<<<<<<<<<<<<<<<<<<<<<<<<<<  
Top.configure(background='white')
f1.configure(background='black')
f2.configure(background='black')

lbltitle= Label (Top,font=('arial',40,'bold'),bd=10,width=40,text='Train Ticket System',justify='center')
lbltitle.grid(row=0,column=0)

#...........................................top right frame.....................................
lblreceit= Label (frametopright,font=('arial',14,'bold'),bd=10,width=31,text='Travelling receits',justify='center')
lblreceit.grid(row=0,column=0)
 
 #....................
lblclass1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Class',justify='center')
lblclass1.grid(row=0,column=0)

lblclass2= Label (framebottomright,relief='sunken',textvariable=class1,font=('arial',14,'bold'),width=8,justify='center')
lblclass2.grid(row=1,column=0)

lblticket1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Ticket',justify='center')
lblticket1.grid(row=0,column=1)

lblticket2= Label (framebottomright,relief='sunken',textvariable=fees,font=('arial',14,'bold'),width=8,justify='center')
lblticket2.grid(row=1,column=1)

lbladult1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Adult',justify='center')
lbladult1.grid(row=0,column=2)

lbladult2= Label (framebottomright,relief='sunken',textvariable=adult,font=('arial',14,'bold'),width=8,justify='center')
lbladult2.grid(row=1,column=2)

lblchild1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Child',justify='center')
lblchild1.grid(row=0,column=3)

lblchild2= Label (framebottomright,textvariable=child,relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblchild2.grid(row=1,column=3)

lblfrom1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='From',justify='center')
lblfrom1 .grid(row=2,column=1)
 
lblfrom2= Label (framebottomright,relief='sunken',textvariable=from1,font=('arial',14,'bold'),width=8,justify='center')
lblfrom2.grid(row=2,column=2)

lblto1= Label (framebottomright,text='To', relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblto1 .grid(row=3,column=1)
 
lblto2= Label (framebottomright,relief='sunken',textvariable=to,font=('arial',14,'bold'),width=8,justify='center')
lblto2.grid(row=3,column=2)

lblprice1= Label (framebottomright,text='Price',relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblprice1.grid(row=3,column=2)

lblprice2= Label (framebottomright,relief='sunken',textvariable=price,font=('arial',14,'bold'),width=8,justify='center')
lblprice2.grid(row=3,column=2)


lblRefNo1= Label (framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Ref No',justify='center')
lblRefNo1 .grid(row=5,column=0)
 
lblRefNo2= Label (framebottomright,textvariable=ref,relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblRefNo2.grid(row=6,column=0)

lblTime1= Label (framebottomright, relief='sunken',font=('arial',14,'bold'),width=8,text='Time',justify='center')
lblTime1 .grid(row=5,column=1)
 
lblTime2= Label (framebottomright,textvariable=time1,relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblTime2.grid(row=6,column=1)

lbldate1= Label (framebottomright,text='Date',relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lbldate1.grid(row=5,column=2)

lbldate2= Label (framebottomright,textvariable=Date1,relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lbldate2.grid(row=6,column=2)

lblroute1= Label (framebottomright,text='Route',relief='sunken',font=('arial',14,'bold'),width=8,justify='center')
lblroute1.grid(row=5,column=3)

lblroute2= Label (framebottomright,relief='sunken',textvariable=route,font=('arial',14,'bold'),width=8,justify='center')
lblroute2.grid(row=6,column=3)

#.......................................date and time........................
Date1.set(time.strftime("%d/%m/%Y"))#date
time1.set(time.strftime("%H:%M:%S"))#time

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>functions for the calculator ...<<<<<<<
 
def btnclick(x):
	global operator
	operator= operator + str(x)
	text_input.set(operator)

def btn_del():
	global operator
	operator = ""
	text_input.set("")

def btn_equal():
	global operator
	answer=str(eval(operator))
	text_input.set(answer)
	operator=""
 
def E_exit():
	msg=messagebox.askyesno("Quit","Do you want to Quit")
	if msg > 0:
		root.destroy()
		return

def Reset():
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	total.set(0)
	sub_total.set(0)
	tax.set(0)

def Clear():
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	total.set(0)
	sub_total.set(0)
	tax.set(0)

    
def travel_cost():
	if var9.get()=="Nairobi" and var1.get()==1 and var4.get()==1:
		Tcost=float(30.5)
		Single=float(var11.get())
		Adult_tax="Ksh"+str((Tcost*Single)*0.03)
		Adult_fees="Ksh"+str(Tcost*Single)
		Total_cost="Ksh"+str((Tcost*Single)+((Tcost*Single)*0.03))
		tax.set(Adult_tax)
		sub_total.set(Adult_fees)
		class1.set("Standard")
		fees.set(Adult_fees)
		child.set("No")
		adult.set("Yes")
		from1.set("Kitale")
		To.set("Nairobi")
		fees.set(Total_cost)
		fees.set(Total_cost)
		route.set("Direct")


		x=random.randint(109,5748)
		randomRef=str(x)
		ref.set("cdk"+randomRef)

	elif(var9.get()=="Nairobi" and var1.get()==1 and var4.get()==0):
		if var9.get()=="Nairobi" and var1.get()==1 and var4.get()==1:
			Tcost=float(27.5)
			Single=float(var11.get())
			child_tax="Ksh"+str((Tcost*Single)*0.03)
			child_fees="Ksh"+str(Tcost*Single)
			Total_cost="Ksh"+str((Tcost*Single)+((Tcost*Single)*0.03))
			tax.set(child_tax)
			sub_total.set(child_fees)
			class1.set("Standard")
			fees.set(child_fees)
			child.set("No")
			adult.set("Yes")
			from1.set("Kitale")
			To.set("Nairobi")
			fees.set(Total_cost)
			fees.set(Total_cost)
			route.set("Direct")


			x=random.randint(109,5748)
			randomRef=str(x)
			ref.set("cdk"+randomRef)





def check_button():
	if (var6.get()==1):
		var11.set("")
		entsingle.configure(state =NORMAL)
	elif (var6.get()==0):
		entsingle.configure(state = DISABLED)
		var11.set("0")
	if (var7.get()==1):
		var8.set("")
		entreturn.configure(state =NORMAL)
	elif (var7.get()==0):
		entreturn.configure(state = DISABLED)
		var8.set("0")


 #>>>>>>>>>>>>>>>>>>>>>..top left1 frames widget.<<<<<<<<<<<<<<<<<<<<<<<
lblclass = Label ( topleft1,font=('arial',20,'bold'),text='Class',bd=8)
lblclass.grid(row=0,column=0,sticky=W)
chkstandard = Checkbutton ( topleft1,font=('arial',20,'bold'),text='Standard',variable=var1,onvalue=1,offvalue=0,bd=8)
chkstandard.grid(row=1,column=0,sticky=W)
chkeconomy = Checkbutton ( topleft1,font=('arial',20,'bold'),text='Economy',variable=var2,onvalue=1,offvalue=0,bd=8)
chkeconomy.grid(row=2,column=0,sticky=W)
chkfirstclass = Checkbutton ( topleft1,font=('arial',20,'bold'),text='First Class',variable=var3,onvalue=1,offvalue=0,bd=8)
chkfirstclass.grid(row=3,column=0,sticky=W)


#>>>>>>>>>>>>>>>>>>>>>..top left3 frames widget.<<<<<<<<<<<<<<<<<<<<<<<

lbldestination = Label ( topleft3,font=('arial',20,'bold'),text='Select a Destination',bd=8)
lbldestination.grid(row=0,column=0,sticky=W,columnspan=2)
lbldestination = Label ( topleft3,font=('arial',20,'bold'),text='Destination',bd=5)
lbldestination.grid(row=1,column=0,sticky=W)
#combobox
cbnDestination=ttk.Combobox(topleft3,textvariable=var9,state='readonly',font=('arial',22,'bold'),width=8)
cbnDestination['value']=('','Nairobi','Eldoret','Nakuru')
cbnDestination.current(0)
cbnDestination.grid(row=1,column=1)

chkAdult = Checkbutton ( topleft3,font=('arial',20,'bold'),text='Adult',variable=var4,onvalue=1,offvalue=0,bd=8)
chkAdult.grid(row=2,column=0,sticky=W)
chkchild = Checkbutton ( topleft3,font=('arial',20,'bold'),text='Child',variable=var5,onvalue=1,offvalue=0,bd=8)
chkchild.grid(row=3,column=0,sticky=W)


 #>>>>>>>>>>>>>>>>>>>>>.tickets.top left2 frames widget.<<<<<<<<<<<<<<<<<<<<<<<

lbltype = Label ( topleft2,font=('arial',20,'bold'),text='Ticket Type',bd=8)
lbltype.grid(row=0,column=0,sticky=W)
chksingle = Checkbutton ( topleft2,font=('arial',20,'bold'),text='Single',variable=var6,onvalue=1,offvalue=0,bd=8)
chksingle.grid(row=1,column=0,sticky=W)
entsingle=Entry(topleft2,font=('arial',20,'bold'),textvariable=var11,bd=2,width=6)
entsingle.grid(row=1,column=1,sticky=W)
chkreturn = Checkbutton ( topleft2,font=('arial',20,'bold'),text='Return',variable=var7,onvalue=1,offvalue=0,bd=8)
chkreturn.grid(row=2,column=0,sticky=W)
entreturn=Entry(topleft2,font=('arial',20,'bold'),textvariable=var8,bd=2,width=6)
entreturn.grid(row=2,column=1,sticky=W)
lblcomment = Label ( topleft2,font=('arial',20,'bold'),text='comments',bd=8)
lblcomment.grid(row=3,column=0,sticky=W)
entrecomment=Entry(topleft2,font=('arial',20,'bold'),textvariable=var10,bd=2,width=6)
entrecomment.grid(row=3,column=1,sticky=W)



#>>>>>>>>>>>>>>>>>>>>calculator creation ...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#...............entry area.................
text_input=StringVar()
txtDisplay=Entry(bottomleft2,font=('arial',10,'bold'),textvariable=text_input,bd=8,bg='powder blue',justify='right')
txtDisplay.grid(columnspan=4)
#...............buttons...............

btn7=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column=0)
btn8=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="8",bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column=1)
btn9=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="9",bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column=2)
add=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column=3)


btn4=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column=0)
btn5=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column=1)
btn6=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column=2)
minus=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column=3)

btn1=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column=0)
btn2=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column=1)
btn3=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column=2)
multiply=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="x",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column=3)


btn0=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column=0)
btnclear=Button(bottomleft2,width=4,fg='black',padx=8,pady=8,font=('arial',10,'bold'),text="del",bg="powder blue",command=btn_del).grid(row=5,column=1)
btnequals=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="=",bg="powder blue",command=btn_equal).grid(row=5,column=2)
divide=Button(bottomleft2,width=4,font=('arial',10,'bold'),pady=8,padx=8,fg='black',text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column=3)

#>>>>>>>>>>>>>>>>>>>>>>>>tax area <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


lbltax = Label ( bottomleft1,font=('arial',15,'bold'),text='Tax',bd=14)
lbltax.grid(row=3,column=2)
enttax=Entry(bottomleft1,font=('arial',15,'bold'),justify='right',bg="#ffffff",textvariable=tax,bd=10,width=6)
enttax.grid(row=3,column=3)

lblsubtotal= Label ( bottomleft1,font=('arial',15,'bold'),text='Sub Total',bd=14)
lblsubtotal.grid(row=4,column=2)
entsubtotal=Entry(bottomleft1,font=('arial',15,'bold'),justify='right',bg="#ffffff",textvariable=sub_total,bd=10,width=6)
entsubtotal.grid(row=4,column=3)

lblTotal = Label ( bottomleft1,font=('arial',15,'bold'),text='Total Tax',bd=14)
lblTotal.grid(row=5,column=2)
entTotal=Entry(bottomleft1,font=('arial',15,'bold'),justify='right',bg="#ffffff",textvariable=total,bd=10,width=6)
entTotal.grid(row=5,column=3)

#lblspace = Label ( bottomleft1,anchor='w',font=('arial',24,'bold'),text='   \n    ',bd=16)
#lblspace.grid(row=6,column=2)

#lblspace = Label ( bottomleft2,anchor='w',font=('arial',24,'bold'),text='   \n    ',bd=16)
#lblspace.grid(row=6,column=4)

#...................................text info........................
#lblreceit = Label ( framebottomright,font=('arial',12,'bold'),text='Receit',bd=14)
#lblreceit.grid(row=9,column=0,sticky=W)

#textreceit = Text ( framebottomright,width=40,height=7,font=('arial',11,'bold'),bg='white',bd=8)
#textreceit.grid(row=10,column=0,columnspan=4)

#.....................space.........
#lblspace = Label ( framebottomright,anchor='w',relief='sunken',font=('arial',24,'bold'),width=34,height=1,justify='center',bd=14)
#lblspace.grid(row=6,column=0,columnspan=4)
#............................buttons................................

btnTotal= Button(framebottomright,text='Total',command=travel_cost,padx=2,pady=2,bd=2,fg='black',font=('arial',14,'bold'),width=6,height=1).grid(row=7,column=0)
btnClear= Button(framebottomright,command=Clear,text='Clear',padx=2,pady=2,bd=2,fg='black',font=('arial',14,'bold'),width=6,height=1).grid(row=7,column=1)
btnReset= Button(framebottomright,command=Reset,text='Reset',padx=2,pady=2,bd=2,fg='black',font=('arial',14,'bold'),width=6,height=1).grid(row=7,column=2)
btnExit= Button(framebottomright,command=E_exit,text='Exit',padx=2,pady=2,bd=2,fg='black',font=('arial',14,'bold'),width=6,height=1).grid(row=7,column=3)


#>>>>>>>>>>>>>>>>>>>>>>>>mainloop <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

root.mainloop()    























 