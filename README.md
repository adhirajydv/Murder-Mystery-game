Project Introduction: A Text-Based Murder Mystery Game

This project is an interactive text-based murder mystery game written in Python. It puts the player in the role of a detective investigating a murder at a grand mansion. The game utilizes a simple command-line interface to guide players through the mansion, allowing them to explore different rooms, gather clues, and interrogate suspects.

Key Features:

Exploration: Players can navigate through various rooms in the mansion, each with its own unique description and potential clues to discover.
Clue Gathering: Hidden within the rooms are clues that players must find to identify the murderer. The game keeps track of found clues to avoid repetition.
Suspect Interrogation: Players can interrogate a set of suspects, each with their own alibi and potential connection to the victim.
Accusation and Resolution: Based on the gathered clues, players make an accusation. The game determines the outcome based on the accuracy of their deduction.
Randomized Suspect Order: The order in which suspects are presented is randomized, adding replayability to the game.
Technical Implementation:

The game is implemented using Python and leverages functions to organize the code and create modularity. Key aspects of the implementation include:

Functions for Rooms: Each room in the mansion is represented by a separate function, handling its unique logic and interactions.
Clue Management: A list is used to store the clues found by the player.
Suspect List: Suspects are stored in a list and their order is randomized using the random.shuffle() function.
Input Validation: The get_choice function ensures that the player enters valid input.
Potential for Expansion:

This project provides a solid foundation for a more complex and engaging murder mystery game. Future enhancements could include:

More Rooms and Clues: Expanding the mansion with additional rooms and hiding more clues would increase the game's depth and challenge.
Dynamic Interrogations: Making interrogations more interactive with branching dialogue options and suspect reactions would create a more immersive experience.
Puzzles and Challenges: Introducing puzzles or riddles within the game would add another layer of complexity and engagement.
Inventory System: Allowing players to collect and use items could open up new possibilities for solving the mystery.
Multiple Endings: Creating different endings based on player choices would increase replayability and provide a more dynamic narrative.
This project demonstrates fundamental programming concepts like functions, conditional statements, loops, and list manipulation in Python. It also showcases the ability to create an engaging interactive narrative within a text-based environment.
