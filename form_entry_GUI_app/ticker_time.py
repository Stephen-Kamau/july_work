from tkinter import*
import time
def tickertime():
	#create a variable to store the time and format it
	clock_time=time.strftime("%A  %H:%M:%S")#A means full day name
	clock.config(text=clock_time)
	#set the number of ticks the clock to tick 
	clock.after(100,tick)
window=Tk()
#create an object for the gui
clock=Label(window,bg="blue",font=("times",100,"bold"))
clock.grid(row=0,column=2)
tickertime()
#call the function
window.mainloop()