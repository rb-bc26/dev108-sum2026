# this is DEV 108 Python Programming Final: Battle Simulator
# [08/16/2026]
# [Reecha Bharali]

import csv
#Reads characters from the CSV file in this final folder
import random

FILENAME = "characters.csv"

def read_characters():
#Reads characters from the CSV file and returns a list of lists
    characters = []
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)                     # skip the header row
            for row in reader:               # outer loop: each line of the CSV
                for i in range(1, 6):        # inner loop: columns 1-5 of THAT row
                     row[i] = int(row[i])
                characters.append(row)      
    except FileNotFoundError:
        print(f"Could not find {FILENAME}. Starting with empty character list.")
    return characters

def write_characters(characters):
#Writes the list of characters back to the CSV file
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Power", "Strength", "Defense", "Wins", "Losses"])
        for char in characters:
            writer.writerow(char)

def display_menu():
#Displays the main menu options to the user
    print("\n--- Main Menu ---")
    print("1. Create a New Character")
    print("2. List All Characters")
    print("3. Search for a Character")
    print("4. Delete a Character")
    print("5. Battle!")
    print("6. Exit")

def create_character(characters):
#Allows the user to create a new character with random stats
    print("\n--- Create Character ---")
    name = input("Enter character name: ").strip()
    
    # Generate random stats

    power = random.randint(50, 150)
    strength = random.randint(10, 30)
    defense = random.randint(5, 20)
    wins = 0
    losses = 0
    
    new_char = [name, power, strength, defense, wins, losses]
    characters.append(new_char)
    write_characters(characters)
    
    print(f"\n{name} has been created!")
    print(f"Stats - Power: {power}, Strength: {strength}, Defense: {defense}")

def list_characters(characters):
#Displays all characters in a formatted table
    print("\n--- Character List ---")
    print(f"{'Name':<15} | {'Power':<5} | {'Strength':<10} | {'Defense':<10} | {'Wins':<5} | {'Losses':<6}")
    print("-" * 65)
    for char in characters:
        print(f"{char[0]:<15} | {char[1]:<5} | {char[2]:<10} | {char[3]:<10} | {char[4]:<5} | {char[5]:<6}")

def search_character(characters):
#Searches for a character by name and displays their stats
    print("\n--- Search ---")
    search_name = input("Enter character name to search: ").strip().lower()
    
    for char in characters:
        if char[0].lower() == search_name:
            print("\nCharacter Found:")
            print(f"Name:     {char[0]}")
            print(f"Power:       {char[1]}")
            print(f"Strength: {char[2]}")
            print(f"Defense:  {char[3]}")
            print(f"Wins:     {char[4]}")
            print(f"Losses:   {char[5]}")
            return
            
    print("Character not found.")

def delete_character(characters):
#Deletes a character from the list after asking for confirmation
    print("\n--- Delete Character ---")
    delete_name = input("Enter the name of the character to delete: ").strip().lower()
    
    for i in range(len(characters)):
        if characters[i][0].lower() == delete_name:
            confirm = input(f"Are you sure you want to delete {characters[i][0]}? (y/n): ").strip().lower()
            if confirm == 'y':
                print(f"{characters[i][0]} has been deleted.")
                characters.pop(i)
                write_characters(characters)
            else:
                print("Deletion canceled.")
            return
            
    print("Character not found.")

def choose_fighter(characters, prompt):
#Helper function to let the user select a character for battle
    while True:
        choice = input(prompt).strip()
        if choice.lower() == 'r':
            return random.choice(characters)
        
        for char in characters:
            if char[0].lower() == choice.lower():
                return char
        print("Invalid character name. Try again.")

def battle(characters):
# Battle characters
    if len(characters) < 2:
        print("Not enough characters to battle.")
        return

    print("\n--- BATTLE ---")

    fighter1 = choose_fighter(characters, "First fighter's name (or 'r' for random): ")
    fighter2 = choose_fighter(characters, "Second fighter's name (or 'r' for random): ")

    # Check if both fighters were actually found
    if fighter1 == None or fighter2 == None:
        print("Could not find one or both names. Battle canceled.")
        return

    print(f"\n{fighter1[0]} VS {fighter2[0]}!")

    power2 = fighter2[1]

    # Fighter 1 attacks ONE time
    damage1 = random.randint(5, fighter1[2])
    power2 -= damage1
    print(f"{fighter1[0]} strikes for {damage1} damage! {fighter2[0]} drops to {power2} Power.")

    # Fighter 2 attacks ONE time
    damage2 = random.randint(5, fighter2[2])
    power1 -= damage2
    print(f"{fighter2[0]} strikes back for {damage2} damage! {fighter1[0]} drops to {power1} Power.")

    # Determine the winner based on who has the most Power left
    print("\n--- Battle Over ---")
    if power1 > power2:
        print(f"{fighter1[0]} WINS with more Power remaining!")
        fighter1[4] += 1  # Add 1 win to fighter 1
        fighter2[5] += 1  # Add 1 loss to fighter 2
    elif power2 > power1:
        print(f"{fighter2[0]} WINS with more Power remaining!")
        fighter2[4] += 1  # Add 1 win to fighter 2
        fighter1[5] += 1  # Add 1 loss to fighter 1
    else:
        print("It's a TIE! No wins or losses recorded.")

    # Save the updated wins and losses to the CSV
    write_characters(characters)

def main():
#Main program loop and logic handling
    print("Welcome to the Character Generator Battle Simulator!")
    characters = read_characters()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            create_character(characters)
        elif choice == "2":
            list_characters(characters)
        elif choice == "3":
            search_character(characters)
        elif choice == "4":
            delete_character(characters)
        elif choice == "5":
            battle(characters)
        elif choice == "6":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()