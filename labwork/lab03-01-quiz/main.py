# this is the starting file for Lab Activity 3
# create your own starting code for the instructions provided 
# DEV 108 Lab Activity 3
# [07/16/2026]
# [Reecha Bharali]
# Create 1) simple 5 question math 
# Create 2) multiple choice quiz

#display title of the program
print("Welcome to the Math Quiz")
print()

# Ask user if they would like to take the quiz
ans =input("Would you like to take this Math Quiz? Y/N ")
if ans.lower() == "y":
    print("Okay let's move forward")
    #initialize score counter variable
    counter=0
    #5 math quiz questions 
    q1=int(input("What is 5 + 5 ? "))
    if q1 == 10:
        print ("10 is correct")
        counter += 1
    else:
        print("Sorry that's incorrect") 

    q2=int(input("What is 10 x 15 ? "))
    if q2 == 150:
        print("150 is correct")
        counter += 1
    else:
        print("Sorry that's incorrect") 
        
    q3=int(input("What is 30 / 3 ?  "))
    if q3 == 10:
        print("10 is correct")
        counter += 1
    else:
        print("Sorry that's incorrect") 
    
    q4=int(input("What is 1500 / 10 ?  "))
    if q4 == 150:
        print("150 is correct")
        counter += 1
    else:
        print("Sorry that's incorrect") 
    
    q5=int(input("What is 33 * 11 ? "))
    if q5 == 3:
        print("3 is correct")
        counter += 1 
    else:
        print("Sorry that's incorrect") 
 # multiple choice quiz       
    q6 = print("Which of the following is neither prime nor composite?")    
    print("A. 1")
    print("B. 2")
    print("C. 3")
    print("D. 4")
    q6 = input("Choose A/B/C/D: ")
    if q6.upper() == "A" :
            print("Correct! 1 & 0 are neither prime nor composite.")
            counter += 1 
    else:
            print("Sorry, that's incorrect.")

    # personalized feedback on test results    
    print("Your score is:", counter)
    if counter == 6:
        print("5/5 & Bonus = Awesome work! You are a Rockstar")
    elif counter == 5:
        print("5/5 = Nice job! Almost 100%.")
    elif counter == 4:
        print("4/5 = Nice job! Almost 100%.")
    elif counter == 3:
        print("3/5 = Keep Studying")
    elif counter == 2:
        print("2/5 = Keep Studying")    
    else:
        print ("1/5 = Maybe this isn't your area of interest?")    
     
elif ans.lower() == "n":
    print("Okay, See you next time") 
else: 
    print("Invalid Entry. Please enter Y/N")

