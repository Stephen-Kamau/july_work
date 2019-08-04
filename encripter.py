#this program encripts the text passed using certain format
def encript():
	x=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>/=-_+#$%&*()[]}{:"\',.'
	key=11
	text=input("Enter the message to be encripted: ")
	new_text=""
	for i in text:
		#loop through the input
		if i in x:
			#test through the charcters found
			position=x.find(i)
			new_position=(position + key) % 85
			new_char=x[new_position]
			new_text+=new_char
	print("Encripted text is : ",new_text)
encript()