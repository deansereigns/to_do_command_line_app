# To-do app Project using Python
usr_input = 'random'

items_list = list()
# A list for storing items

# There are 4 basic operations that the user can perform
# 1. Add a new item
# 2. Mark an item as Done
# 3. View Items in the list
# 4. Exit




def Menu():
	print("Menu:")
	print("1. Add a new item.")
	print("2. View Items in the list.")
	print("3. Mark an item as Done.")
	print("4. Exit.")
# Menu Function Displaying various operations to user.

while usr_input != '4':

	Menu()
	usr_input = input("Enter Your Choice: ")

	if usr_input == '1':
		item = input("What is to be done.\n")
		print
		items_list.append(item)
		print("Added item:", item)

	elif usr_input == '2':
		print("List of TO-DO Items: ")
		for items in items_list:
			print(items)

	elif usr_input == '3':
		item = input("What is to be marked as Done\n")

		# if item is present in items_list then it is removed from the list
		# else print item does not exist in the list

		if item in items_list:
			items_list.remove(item)
			print("Removed item:", item)
		else:
		    print("Item does not exist in the to-do list ")
	
	    
	elif usr_input == '4':
	    print("Hope Your Experience was good. ")    	
	    print("Thanks & GOOD BYE")
