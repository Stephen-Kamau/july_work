from tkinter import*
import time

#cretaed by Stephen Kamau
#Email::stiveckamash@gmailcom   or stephenkamau714@gmail.com
#GUI projec for the june end month
#call: 0705698768   
#project name calculator 


#========================window interface definition===============



time_now=time.asctime(time.localtime(time.time()))
win=Tk()
win.geometry('370x550')
x=("The New Gen CALCULATOR..Time:",time_now)
win.title(x)
win.resizable(width=False,height=False)

#========================frame definitions==================

#top frame
top=Frame(win,width=500,height=50,bg='yellow',relief=RAISED)
top.pack(side=TOP)

#name for the top frame
label1=Label(top,text='STEVE CALCULATOR',fg='blue',font=('arial',20,'bold'))
label1.grid(row=0,column=0)
#farme containing the numbers of caclualtor inputs
frame=Frame(win,width=500,height=450,bg='powder blue',relief=SUNKEN)
frame.pack(side=LEFT)

#definition for the input
text_in=StringVar()

entry_bar=Entry(frame,textvariable=text_in,font=('arial',20,'bold'),bg='white',insertwidth=3,justify='right',bd=30,relief=RAISED)
entry_bar.grid(columnspan=5)


#==============onclick definiton============

#Number display on the entry box
operator=""
def btn_click(x):
	global operator
	operator=operator + str(x)
	text_in.set(operator)

#btn for clearing the screen
def clear_btn():
	global operator
	operator=""
	text_in.set(operator)

#btn for the evaluation
def Equal_btn():
	global operator
	try:
		equal=str(eval(operator))
		text_in.set(equal)
		operator=""
		
	except Exception as e:
		text_in.set(e)


#==========================button definition is here======================
#row one with 7...8...9..+ inputs
btn_7=Button(frame,font=('arial',20,'bold'),text='7',bd=8,padx=16,pady=16,command=lambda:btn_click(7),fg='red')
btn_7.grid(row=2,column=0)
btn_8=Button(frame,font=('arial',20,'bold'),text='8',bd=8,padx=16,pady=16,command=lambda:btn_click(8),fg='red')
btn_8.grid(row=2,column=1)
btn_9=Button(frame,font=('arial',20,'bold'),text='9',bd=8,padx=16,pady=16,command=lambda:btn_click(9),fg='red')
btn_9.grid(row=2,column=2)
btn_add=Button(frame,font=('arial',20,'bold'),text='+',bd=8,padx=16,pady=16,command=lambda:btn_click('+'),fg='red')
btn_add.grid(row=2,column=3)

#row two with 4...5....6...-
btn_4=Button(frame,font=('arial',20,'bold'),text='4',bd=8,padx=16,pady=16,command=lambda:btn_click(4),fg='red')
btn_4.grid(row=3,column=0)
btn_5=Button(frame,font=('arial',20,'bold'),text='5',bd=8,padx=16,pady=16,command=lambda:btn_click(5),fg='red')
btn_5.grid(row=3,column=1)
btn_6=Button(frame,font=('arial',20,'bold'),text='6',bd=8,padx=16,pady=16,command=lambda:btn_click(6),fg='red')
btn_6.grid(row=3,column=2)
btn_minus=Button(frame,font=('arial',20,'bold'),text='-',bd=8,padx=16,pady=16,command=lambda:btn_click('-'),fg='red')
btn_minus.grid(row=3,column=3)

#row three with 1...2....3...*
btn_1=Button(frame,font=('arial',20,'bold'),text='1',bd=8,padx=16,pady=16,command=lambda:btn_click(1),fg='red')
btn_1.grid(row=4,column=0)
btn_2=Button(frame,font=('arial',20,'bold'),text='2',bd=8,padx=16,pady=16,command=lambda:btn_click(2),fg='red')
btn_2.grid(row=4,column=1)
btn_3=Button(frame,font=('arial',20,'bold'),text='3',bd=8,padx=16,pady=16,command=lambda:btn_click(3),fg='red')
btn_3.grid(row=4,column=2)
btn_times=Button(frame,font=('arial',20,'bold'),text='*',bd=8,padx=16,pady=16,command=lambda:btn_click('*'),fg='red')
btn_times.grid(row=4,column=3)

#row foru with 0.....clear as C.....=....../
btn_0=Button(frame,font=('arial',20,'bold'),text='0',bd=8,padx=16,pady=16,command=lambda:btn_click(0),fg='red')
btn_0.grid(row=5,column=0)
btn_clear=Button(frame,font=('arial',20,'bold'),text='C',bd=8,padx=16,pady=16,fg='purple',command=clear_btn)
btn_clear.grid(row=5,column=1)
btn_equal=Button(frame,font=('arial',20,'bold'),text='=',bd=8,padx=16,pady=16,command=Equal_btn,fg='red')
btn_equal.grid(row=5,column=2)
btn_divide=Button(frame,font=('arial',20,'bold'),text='/',bd=8,padx=16,pady=16,command=lambda:btn_click('/'),fg='red')
btn_divide.grid(row=5,column=3)




win.mainloop()