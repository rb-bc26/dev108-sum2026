# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score.lower() == "x": # Change: exit the loop first, before trying any number conversion + use lower()
        break
    test_score = float(test_score) #for decimal scores

    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1 #Change: Counter runs in if loop
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

if counter > 0:
# calculate average score
    average_score = round(score_total / counter,1) #Change: to one decimal place
                    
    # format and display the result
    print("======================")
    print("Total Score:", score_total,
        "\nAverage Score:", average_score)
    print()
else:
    print("No scores were entered")

#When user types x as the first input
print("Hope you have a goodday. Bye")