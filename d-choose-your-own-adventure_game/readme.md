Project #4: Choose Your Own Adventure Game 🗺️
 * Client Deliverable: A branching narrative text game implemented using nested conditional statements (if/elif/else).
 * Core Requirements:
   * The narrative must begin with a clear scenario and at least two distinct paths (e.g., "left" or "right").
   * Each path must lead to further choices, creating a minimum of 8 unique final outcomes (endings).
   * All user inputs must be processed to handle variations in spelling and capitalization.
 * Success Metrics (Worthy & Respectable Additions):
   * State Tracking: Introduce a simple "Inventory" or "Health" variable (e.g., gold = 0, health = 100) that is affected by choices and can lead to specific, locked endings (e.g., "You didn't have enough gold, game over.").
   * Function Decomposition: Implement a function for each major decision point or location to keep the code clean and easy to follow.
   * Dynamic Descriptions: Use f-strings or string formatting to dynamically include the user's name (collected at the start) throughout the narrative.

# Rock, Paper, Scissor game

> A command-line game where the user plays rock, paper or scissors against a computer opponent.

### Requirements :  
- Use the random module for the computer's choice selection.
- Allow the user to input their choice. Handle case-sensitive (eg. 'r','Rock','R' all works)
    - Re-prompt if the user inputs a wrong input
- Implement the win/loss logic (rock beats scissors, scissors beats paper, paper beats rock)
- Keep scores over multiple round (first to 3 wins)
- Upon win show the final summary