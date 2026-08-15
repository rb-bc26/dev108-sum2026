# starting file for Lab 5
# this is DEV 108
# [07/24/2026]
# [Reecha Bharali]
# Guess the Number program from our textbook

# Import the 'random' module so we can generate a random number for the player to guess.
import random

# Print the game's title
def display_title():
    print("Guess the number!")
    print()

 # Ask the player for their name and store what they typ
def get_name():
    player_name = input("What is your name?")
    print ("Hello", player_name)
    print()

def play_game(wins): 
    # Ask which difficulty level the player wants
    level = input("What level game would you want to play? Enter E=Easy, M=Medium , H=Hard. Enter : ")   
    # Set the range of numbers (max_number) and how many guesses (tries)
    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 100
        tries = 8
    elif level.lower() == "h":
        max_number = 1000
        tries = 10
    else:
        print("Invalid input. Try again. Enter E=Easy, M=Medium , H=Hard ")

# Pick a random whole number between 1 and max_numbe
    number = random.randint(1, max_number)
    print(f"I'm thinking of a number from 1 to {max_number}\n")
    count = 1

    while count <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print ("You guessed it in " + str (count) + "tries. \n" )
            wins += 1 
            print("You have won ", wins , "games.")
            return wins
    else:
        print ("Sorry you ran out of guesses. The number was ", number)
     
def main():
    display_title()
    get_name()
    #initialize wins
    wins = 0
    
    # 'again' controls the replay loop; start it as "y" so we play at least once
    again = "y"
    while again.lower() == "y":
        play_game(wins)
        # Ask whether to play again; anything other than "y" ends the loop
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
