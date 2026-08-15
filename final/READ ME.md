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

# Test Cases
Testing used the starting roster in `characters.csv`:
Name,Power,Strength,Defense,Wins,Losses
Snake Plant,100,20,10,0,0
ZZ Plant,120,25,5,0,0
Spider Plant,80,15,15,0,0
Cast Iron Plant,150,30,20,0,0
Pothos,70,15,5,0,0
Yarrow,110,15,10,0,0

Each test case below was run against this roster from a clean copy of the CSV.

| # | Feature | Input | Expected Result | Actual Result | Pass/Fail |

| 1 | Create a New Character | Menu `1`, name `Reecha Bharali` | New character appended to the list and to `characters.csv` with random Power (50-150), Strength (10-30), Defense (5-20), Wins/Losses = 0 | `Reecha Bharali` created with Power 143, Strength 22, Defense 19, Wins 0, Losses 0; row appended to CSV | Pass |

| 2 | List All Characters | Menu `2` | All 6 characters printed in a tab-aligned table | All 6 rows displayed correctly with header and stats | Pass |

| 3 | Search - character found | Menu `3`, name `Snake Plant` | Full stat block printed for Snake Plant | Displayed Name, Power 100, Strength 20, Defense 10, Wins 0, Losses 0 | Pass |

| 4 | Search - character not found | Menu `3`, name `Ghost Plant` | "Character not found." printed | "Character not found." printed as expected | Pass |

| 5 | Delete - cancel | Menu `4`, name `Reecha Bharali`, confirm `n` | Character kept; "Deletion canceled." printed; CSV unchanged | Character kept, correct message printed, CSV unchanged | Pass |

| 6 | Delete - confirm | Menu `4`, name `Reecha Bharali`, confirm `y` | Character removed from list and CSV | "Reecha Bharali has been deleted." printed; row removed from CSV | Pass |

| 7 | Delete - character not found | Menu `4`, name `Ghost Plant` | "Character not found." printed | "Character not found." printed as expected | Pass |

| 8 | Battle - two named fighters | Menu `5`, `Snake Plant`, `ZZ Plant` | Each fighter deals one hit; higher remaining Power wins; winner's Wins +1, loser's Losses +1; result saved to CSV | ZZ Plant won 113 to 94; ZZ Plant Wins → 1, Snake Plant Losses → 1; CSV updated | Pass |

| 9 | Invalid menu choice | Menu `9` | "Invalid input. Please enter a number from 1 to 6." printed, menu redisplayed | Correct message printed, program did not crash | Pass |

| 10 | Exit | Menu `6` | "Thanks for playing! Goodbye." printed, program ends | Program exited cleanly | Pass |


## AI Usage Disclosure
Used Claude to assist with fixing indentation errors by using debugging code logic in the Python programming.  Used AI to format test cases from word file to .md file due to formatting issues.
