#simple progarm to store items in dictionary

suitcase_content={
    'pants':2,
	'trousers':5,
	'shirts':7,
	'vest':9,
	'socks':9,
	'shows':3,
	'ties':4,
	'handkerchief':2
	
}
#print(suitcase_content,'\n')   to print the whole list....
#outputting the content in each line...
for item in suitcase_content:
	print(item, ":",suitcase_content[item])