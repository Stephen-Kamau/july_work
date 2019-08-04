#simple shopping basket

#create an empty dictionary
shop_basket={}
#create empty lists to store the quantity size and item name
quantities=[]
items=[]
#print the menu for the shop
print("""
Shopping Options
----------------
1: Add item(s).
2:Remove item(s).
3:View the shopping Basket.
4:Exit the shop.
	""")
#request the option from the user
option=input("Please select the Shopping option: ")
try:#check ooption to be integer
	option=int(option)
except:
	print("Please enter the integer numbers only: ")

#check the number in range needed
if (option > 0) :
	if option==1:
		item=input("Please enter the item you want to shop: ")
		#quantity=int(input("please enter the quantity of the item you selected: "))
		#shop_basket[item]=quantity
		if item in shop_basket:
			print("Item already found on uour shoopping list:")
			x=int(input("What do you want to do...enter Y/y to update:"))
			if x==y or x==Y :
				quantity=int(input("please enter the quantity of the item you selected: "))
				#add the items to the dictionary
				shop_basket[item]=quantity

			
		else:
			quantity=int(input("please enter the quantity of the item you selected: "))
			quantities.append(quantity)
			items.append(item)
			#use zip function to make the two list dictionaries
			shop_basket=dict(zip(items,quantities))
			print(shop_basket)

	elif option==2:
		item=input("Enter the item you wish to remove: ")
		del(shop_basket[item])
		print("you successefully removed %s", item)
	elif option==3:
		if len(shop_basket) != 0 :
			for goods in shop_basket:
				print(goods , ':' , shop_basket[goods])
		else:
			print("Opps The Shopping List is Empty: ")
	elif option==4:
		print("Exiting.......")
else:
	print("Shopping Closed Temporarily")
