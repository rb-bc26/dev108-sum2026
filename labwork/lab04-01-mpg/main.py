# this is DEV 108 Lab4 lab04-01-mpg 
# [07/23/2026]
# [Reecha Bharali]

# display a welcome message
print("The Miles Per Gallon application")
print()

#setting a default value
repeat_mpg = "y"

#setting choice for while loop
while repeat_mpg.lower() == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter price per gallon:  "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        mpg = round((miles_driven / gallons_used), 2)
        tgc = round((gallons_used * cost_per_gallon), 2)
        cpm = round(( (gallons_used *  cost_per_gallon) / miles_driven),2)
        print()
        print("Miles Per Gallon: ", mpg)
        print("Total Gas Cost  : ", tgc)
        print("Cost per mile   : ", cpm )
        print()
#Infinite Loop
    repeat_mpg = input("Would you like to calculate for another trip. Type Y/N ")

print()
print("Bye")

