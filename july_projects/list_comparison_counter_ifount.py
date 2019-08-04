import random
#declare the empty lists
xl=[]
yl=[]
#declare the count variable
count=0
#generate ten numbers randomly and add them to the list
for x in range(1,10):
	x=random.randint(0,20)
	xl.append(x)
#generate another ten numbers randomly and add them to the list
for y in range(1,10):
	y=random.randint(0,25)
	yl.append(y)
#print list xl
print(yl)
#print list with values of xl
print(xl)

print()
print()
#compaire the two list and update the count to see how many matches from the two lists
for x in xl:
	if x in yl:
		count = count + 1
print(count)
