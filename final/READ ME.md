# DEV 108 Python Programming Final: Battle Simulator
Last Date Edited: 08/16/2026  
by Reecha Bharali

# Description
The program allows users to create characters with randomly generated stats (Power, Strength, Defense), save them to a CSV file (`characters.csv`), and manage the character roster. Users can list, search for, and delete characters, as well as battle two characters. Battle results- Wins and Losses; are saved.

# Program Features
1. Create a New Character: Generates a character with random Power, Strength, and Defense stats.
2. List All Characters: Displays all characters and their current stats in a formatted table.
3. Search for a Character: Lookup characters
4. Delete a Character
5. Battle: Choose two characters to fight. The winner is determined based on the power remaining after one round of attacks. Win/Loss records are updated accordingly.

# Three Test Cases
Testing used the starting roster in `characters.csv`:
Name,Power,Strength,Defense,Wins,Losses
Snake Plant,100,20,10,0,0
ZZ Plant,120,25,5,0,0
Spider Plant,80,15,15,0,0
Cast Iron Plant,150,30,20,0,0
Pothos,70,15,5,0,0
Yarrow,110,15,10,0,0

| # | Feature | Input | Expected Result | Actual Result | Pass/Fail |

| 1 | List All Characters | Menu `2` | All 6 characters printed in a tab-aligned table | All 6 rows displayed correctly with header and stats | Pass |

| 2 | Search - character found | Menu `3`, name `Snake Plant` | Full stat block printed for Snake Plant | Displayed Name, Power 100, Strength 20, Defense 10, Wins 0, Losses 0 | Pass |

| 3 | Battle - two named fighters | Menu `5`, `Snake Plant`, `ZZ Plant` | Each fighter deals one hit; higher remaining Power wins; winner's Wins +1, loser's Losses +1; result saved to CSV | ZZ Plant won 113 to 94; ZZ Plant Wins → 1, Snake Plant Losses → 1; CSV updated | Pass |

## AI Usage Disclosure
Used Claude to assist with fixing indentation errors by using debugging code logic in the Python programming.  Used AI to format test cases from word file to .md file due to formatting issues.
