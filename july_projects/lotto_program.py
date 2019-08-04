#@programmer:steve
#email: stiveckamash@gmail.com
#number: +254705698768
#@program name : LOTTO PROGRAM
#A program that shows the the basic principles 
#on which lotto works
#What one needs to do:
    #select seven numbers from 1 - 49
    #but this program will only range from 0 to 16
    #the program then randomly sets its seven values in the range
    #they are then compaired
    #then it shows how many numbers you matched coreectly
#import the random module
import random
#declare an empty list to store valuse entered
values=[]
#an empty list declaration to store values randomly selected
numbers=[]
print("LOTTO PROGRAM")
print(............................................)

print("Enter your seven guesses for number between 0 to 15: ")
# make the user to enter seven inputs using for loop
for y in range(1,8):
	num=input()
	#use try exception to check that interger values are the one appended to the list
	try:
		num=int(num)

		
	except :
		print("Invalid input   ")
    #check whether the values are in the range given
    #numbers only in the range are the one appended
	if int(num) >= 0 and int(num) < 16 :
		numbers.append(num)
#check whether the inputs is maximum
if len(numbers) < 7 :
	print("I Am Sorry Please check on your values again::")
	print("Check whether some values you entered are out of range 0-15::")
else:
	print("Successfully send your guesses ")

	count=0
	#choose randomly using the module and for loop to selecte seven integers
	for x in range(1,8):
		value=random.randint(0,15)
		values.append(value)
#check if the values you entered are found in the number generated
#if it is fount the count variable is updated
	for num in numbers:
		if num in values:
			count = count + 1

#print the results to the user
if count == 0:
	print("Regretifully you scored nothing:")
	print("Please recharge your line and play again:")
	print("Good Luck!")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)
elif count == 1 :
	print("You scored one")
	print("Keep on playing to improve your chances of winning")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 2 :
	print("You scored two")
	print("Keep on playing to improve your chances of winning")
	print("GoodLuck on your next play")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 3 :
	print("You scored three")
	print("Keep on playing to improve your chances of winning")
	print("You were almost winning")
	print("You seems to win next time")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 4 :
	print(" CONGLATULATIONS! CONGLATULATIONS! You scored four")
	print("YOU WON KSH. ",random.randint(3000,299000))
	print("Keep on playing to improve your chances of winning biigers things")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 5 :
	print(" CONGLATULATIONS! CONGLATULATIONS! You scored five")
	print("YOU WON KSH. ",random.randint(300000,4000000))
	print("Keep on playing to improve your chances of winning tne mega lotto")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 6 :
	print(" CONGLATULATIONS! CONGLATULATIONS! You Failed only one")
	print("YOU WON KSH. ",random.randint(3000000,40000000))
	print("Keep on playing to improve your chances of winning tne mega lotto")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

elif count == 7 :
	print(" CONGLATULATIONS! CONGLATULATIONS! You scored five")
	print(" CONGLATULATIONS! CONGLATULATIONS!")
	print(" CONGLATULATIONS! CONGLATULATIONS!")
	print(" CONGLATULATIONS! CONGLATULATIONS!")
	print("YOU WON KSH.100,000,000 ")
	print("YOU are our currently millionaire: ")
	print("Here is the list you entered and the values for the lotto")
	print("Your Guesses numbers are : ",numbers)
	print("Machine Predicted LOTTO numbers are : ",values)

else:
	print()