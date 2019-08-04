#It takes temperature recording for a particular period of time and draw a line graph for it
#inputs of temp from the user are stored in list
#lets start
import matplotlib.pyplot as pt
import numpy as np

def get_Input():
	temp=[]
	try:
		x=int(input("Enter the number of days you wish to entee\n \
			their temperature records: "))
	except Exception as e:
		raise e
	print("Enter the data for the temperature for %s days: ",x)
	while len(temp) < int(x):
		temp_data=int(input())
		try:
			temp_data=int(temp_data)
		except Exception as e:
			raise e
		temp.append(temp_data)
	pt.title("TEMPERATURE PLOTTER")
	pt.xlabel("DAYS")
	pt.ylabel('Temp in degree celcious')
	pt.plot(temp)
	#pt.savefig("temp.png")
	pt.show()
get_Input()

