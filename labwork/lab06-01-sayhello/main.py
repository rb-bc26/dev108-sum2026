# starting file for lab 6
# this is DEV 108
# [07/26/2026]
# [Reecha Bharali]

# Import my own module nameformat.py
import nameformat

print("The Name Format Module")
print("Hello!")

# User input only one time, before the loop starts
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

#a menu system and give the users a choice of which output format they would like to see
print()
print("===== NAME FORMAT MENU =====")
print("1- Say Hello")
print("2- Full Name")
print("3- Last Name First")
print("4- View Documentation")
print("5- Exit")
print("============================")

#the loop
while True:
    choice = input("What do you want to view? Enter your choice (1-5): ")
 
    if choice == "1":
        # Call the function, store what it RETURNS, then print it.
        result = nameformat.sayHello(firstName)
        print(result)
 
    elif choice == "2":
        result = nameformat.fullName(firstName, lastName)
        print(result)
 
    elif choice == "3":
        result = nameformat.lastNameFirst(firstName, lastName)
        print(result)
 
    elif choice == "4":
        # help() prints the docstring written inside each function.
        print()
        print("--- MODULE DOCUMENTATION ---")
        help(nameformat.sayHello)
        help(nameformat.fullName)
        help(nameformat.lastNameFirst)
 
    elif choice == "5":
        # break is what actually ends the while loop.
        print("Thank you for using the Name Formatter. Goodbye!")
        break
 
    else:
        # Runs when the user types anything other than 1-5.
        print("Sorry, that is not a valid choice. Please enter 1-5.")