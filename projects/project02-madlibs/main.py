# starting file for Project Madlib
# this is DEV 108
# [07/26/2026]
# [Reecha Bharali]

# Output title for the game.
print("==================================================")
print("       Welcome to Madlabs Story Generator")
print("==================================================")

# Ask if the user would like to play, validate y/n
play = input("Would you like to play the game? Please enter Y or N. ").lower()
while play != "y" and play != "n":
    print("Invalid entry!")
    play = input("Would you like to play the game? Please enter Y or N. ").lower()

if play == "n":
    print("Maybe next time. Goodbye!")
else:
    # Ask for the player's name. Greet the player.
    name = input("First, what is your name? ")
    print("Hello,", name + "! Let's make a story.")

    # initializing variables for counting the story and setting default
    story_count = 0
    play_again = "y"

    # main game loop - repeats while the player wants to play
    while play_again == "y":
        # show the menu, then ask for the choice, validate a/b
        print()
        print("Which story would you like?")
        print("  a. A Day at the Zoo")
        print("  b. The Haunted House")
        choice = input("What is your choice (a/b)? ").lower()
        while choice != "a" and choice != "b":
            print("Please enter a valid input. Please enter A or B.")
            choice = input("What is your choice (a/b)? ").lower()

        # story a variable input
        if choice == "a":
            print("Great! I need some words from you.")
            adjective = input("1) Give me an adjective: ")
            animal = input("2) Give me a type of animal: ")
            food = input("3) What is a food you like? ")
            number = int(input("4) Give me a number from 2 to 20: "))
            verb_ing = input("5) Give me a verb ending in -ing: ")
            friend = input("6) Name of a friend or family member: ")
        #print story
            print()
            print(name + ", here is your story:")
            print("==================================================")
            print("One", adjective, "morning, you and", friend, "visit the zoo.")
            print("The first thing you see is a giant", animal, "eating", food + ".")
            print("It swallows", number, "pieces in one bite!")
            print("The zookeeper says it spends all day", verb_ing + ".")
            print(friend, "laughs so hard you both get kicked out. Worth it.")
            print("==================================================")

        # story b variable input
        else:
            print("Spooky choice! I need some words from you.")
            place = input("1) Name a room in a house: ")
            noun = input("2) Give me a noun (an object): ")
            scary_adj = input("3) Give me a scary adjective: ")
            sound = input("4) Give me a sound (like BOO or CREAK): ")
            number2 = int(input("5) Give me a number from 1 to 12: "))
            verb = input("6) Give me a verb: ")
        #print story
            print()
            print(name + ", here is your story:")
            print("==================================================")
            print("At exactly", number2, "o'clock, you enter the", scary_adj, "house.")
            print("In the", place + ", a", noun, "starts to", verb, "all by itself.")
            print("From the walls you hear a loud", sound + "!")
            print("You run out screaming and never look back.")
            print("==================================================")

        # count number of stories and display before asking to play again
        story_count = story_count + 1
        print("You have created", story_count, "story(s).")

        # ask to play again, validate y/n
        play_again = input("Would you like to play again (y/n)? ").lower()
        while play_again != "y" and play_again != "n":
            print("Please enter y or n.")
            play_again = input("Would you like to play again (y/n)? ").lower()

    print("Thanks for playing,", name + "! You made", story_count, "story(s).")