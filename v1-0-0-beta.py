"""
© Copyright [Sigmapages] Warning: Do not copy my idea, we have license
 """
while True:
    user = input("Type(0, 1, 2, 3)")
    if int(user) == 1: 
	    print("a")
    elif int(user) == 2:
	    print("b")
    elif int(user) == 3:
        print("c")
    elif int(user) == 0:
    	print(" ")
    elif user.lower == "quit":
    	break
    else: 
        print("The beta version is limited")