# this is DEV 108 Programming Programming Project 3: Random Character Generator
# [08/02/2026]
# [Reecha Bharali]

# Import the random module so we can generate random numbers and pick random items
import random

# FUNCTION 1- Generates random stats for the character
def generate_stats(plant_name):
    print(f"\nWe have generated stats for your plant, {plant_name}. They are listed below:")
    
    # Using a list for possible plant types
    plant_types = ["Aloe Vera", "Snake Plant", "Monsterra" , "Money Plant" , "Rubber Plant " ]
    
    # Pick a random character type from our list
    chosen_type = random.choice(plant_types)
    
    # Generate 5+ random stats using the random module
    hit_points = random.randint(50, 100)
    strength = random.randint(1, 10)
    wisdom = random.randint(1, 10)
    dexterity = random.randint(1, 10)
    charisma = random.randint(1, 10)
    
  # Print the plant sheet. \t inserts a tab to line up the columns.
    print("~*~*~Plant Sheet~*~*~")
    print(f"Name:\t\t\t{plant_name}")
    print(f"Protected Species:\t{chosen_type}")
    print(f"Hit Points:\t\t{hit_points}")
    print(f"Strength:\t\t{strength}")
    print(f"Wisdom:\t\t\t{wisdom}")
    print(f"Dexterity:\t\t{dexterity}")
    print(f"Charisma:\t\t{charisma}")
    print("======================")

    # Return stats as a list. Order must match the index
    # constants above: NAME, TYPE, HP, STRENGTH.
    stats = [
        plant_name,     # 0 NAME
        chosen_type,    # 1 TYPE
        hit_points,     # 2 HP
        strength,       # 3 STRENGTH
        wisdom,         # 4
        dexterity,      # 5
        charisma        # 6
    ]
    return stats


# FUNCTION 2- This function takes our player's stats and runs a loop against an enemy
def run_battle(player):
    print("\n*****************************")
    print("            BATTLE           ")
    print("*****************************")
    
    # Create a random enemy
    enemy_names = ["Overwatering", "Darkness", "No Fertilizer" , "Fungi"]
    enemy_name = random.choice(enemy_names)
    enemy_hp = random.randint(50, 100)
    enemy_strength = random.randint(1, 10)
    
    print(f"Enemy Appears: {enemy_name} (HP: {enemy_hp})")
    print(f"You: {player['name']} ({player['type']}) (HP: {player['hp']})")
    print("*****************************")
    
    # Loop that carries out the battle until someone's HP falls to 0 or below
    while player["hp"] > 0 and enemy_hp > 0:
        # Player attacks enemy using their strength stat
        player_damage = random.randint(1, player["strength"] * 2)
        enemy_hp -= player_damage
        
        # Enemy attacks player using their strength stat
        enemy_damage = random.randint(1, enemy_strength * 2)
        player["hp"] -= enemy_damage
        
        print(f"\n{player['name']} attacks {enemy_name} for {player_damage} damage!")
        print(f"{enemy_name} counter-attacks {player['name']} for {enemy_damage} damage!")
        print(f"-> Your HP: {player['hp']} | Enemy HP: {enemy_hp}")
    
    print("\n*****************************")
    # Determine the winner using if/else statements
    if player["hp"] <= 0 and enemy_hp <= 0:
        print("Tie! Both Knocked out.")
    elif player["hp"] > 0:
        print(f"Victory! {player['name']} defeated {enemy_name}!")
    else:
        print(f"Defeat! {enemy_name} defeated {player['name']}...")
    print("*****************************")


# --- MAIN PROGRAM LOOP ---
def main():
    print("*****************************")
    print("|Random Plant Protector! |")
    print("*****************************")
    
    # Ask if the user would like to generate a character
    play_game = input("Would you like to create a Plant Protector? (y/n): ").lower()
    
    while play_game == 'y':
        # Ask for a character name
        char_name = input("What name would you like to use for your Plant Protector?: ")
        
        # Call Function 1 and pass the character name as a parameter
        player_stats = generate_stats(char_name)
        
        # Ask if the user would like to battle an enemy with their character
        want_battle = input("Would you like to battle an enemy with this character? (y/n): ").lower()
        if want_battle == 'y':
            run_battle(player_stats)
        
        # Ask if the user would like to generate a different character
        play_game = input("\nWould you like to generate a new character? (y/n): ").lower()

    print("\nThank you for playing the Random Plant Protector! Goodbye.")

# Start the main program
main()