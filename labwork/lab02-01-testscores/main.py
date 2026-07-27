# Instructions for Exercise 2.2
# DEV 108 Lab Activity 2
# [07/11/2026]
# [Reecha Bharali]
# Modify the Test Scores program so that it saves the three scores input into variables named score1, score2, and score 3. Then, add these scores to the total_score variable, instead of adding the entries to the total_score variable without ever saving them.

# Starting Code for Exercise 2.2

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1=int(input("Enter test score: "))
score2=int(input("Enter test score: "))
score3=int(input("Enter test score: "))
print("======================")

#calculate totat and acerage score
total_score = score1+score2+score3
average_score=round((score1+score2+score3)/3,2)

#print scores
print( "Your Scores:", score1 + score2 + score3 )
print("Total Score:", total_score)
print("Average Score:", average_score)

#print message 
print()
print("Bye")
