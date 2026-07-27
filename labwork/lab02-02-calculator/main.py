# this is the starting file for Lab Activity 2.2
# create your own starting code for the instructions provided 
# DEV 108 Lab Activity 2
# [07/11/2026]
# [Reecha Bharali]
# Create a simple program for Area and Perimeter

#display a welcome message
print("The Area and Perimeter program")

#get input from user 
length = int(input("Please enter the length:\t \t"))
breadth = int(input("Please enter the breadth:\t \t"))

# calculate area and perimeter
Area1= length * breadth
Perimeter1= 2*length + 2*breadth

#print area and perimeter
print()
print("Area =", Area1)
print("Perimeter =", Perimeter1)
print()

# display end message
print("Thanks for using this program!")