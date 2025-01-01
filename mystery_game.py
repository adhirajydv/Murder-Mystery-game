import random

def intro():
  """Displays the game's introduction."""
  print("\nWelcome to the Murder Mystery Mansion!")
  print("You are a detective called to investigate a murder at a grand mansion.")
  print("Your task is to explore the mansion, interrogate the suspects, and gather clues to identify the murderer.")
  print("Can you solve the mystery and bring the culprit to justice?\n")

def create_character():
  """Allows the player to create their character."""
  name = input("Enter your detective's name: ")
  print(f"\nDetective {name}, the fate of the case rests on your shoulders!\n")
  return name

def get_choice(options):
  """Displays options and gets valid player choice."""
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
  while True:
    try:
      choice = int(input("Enter your choice: "))
      if 1 <= choice <= len(options):
        return choice
      else:
        print("Invalid choice. Please enter a number from the list.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def room_entrance(clues):
  """Handles the entrance room logic."""
  print("\nYou stand in the grand entrance hall of the mansion.")
  print("There are doors leading to the library (left), the dining room (right), and a grand staircase (ahead).")
  choice = get_choice(["Go left (library)", "Go right (dining room)", "Go ahead (staircase)"])
  if choice == 1:
    return "library", clues
  elif choice == 2:
    return "dining_room", clues
  else:
    return "staircase", clues

def room_library(clues):
  """Handles the library room logic."""
  print("\nYou enter the library, filled with dusty books and a large fireplace.")
  if "book_clue" not in clues:
    print("You notice a book sticking out slightly from the shelf. You pull it out and a piece of paper falls out.")
    print("It's a torn piece of a letter, mentioning a secret meeting in the garden.")
    clues.append("book_clue")
  else:
    print("The library seems undisturbed.")
  print("There is a door leading back to the entrance hall.")
  choice = get_choice(["Go back to the entrance hall"])
  return "entrance", clues  # Return "entrance" to go back

def room_dining_room(clues):
  """Handles the dining room logic."""
  print("\nYou enter the dining room, where a large table is set for a meal that was never eaten.")
  if "wine_clue" not in clues:
    print("You examine the wine glasses on the table and notice one has a different lipstick stain than the others.")
    print("This could be a clue!")
    clues.append("wine_clue")
  else:
    print("The dining room appears as you left it.")
  print("There is a door leading back to the entrance hall.")
  choice = get_choice(["Go back to the entrance hall"])
  return "entrance", clues  # Return "entrance" to go back

def room_staircase(clues):
  """Handles the staircase room logic."""
  print("\nYou ascend the grand staircase, leading to the upper floor.")
  print("There are doors leading to the master bedroom (left) and the guest bedroom (right).")
  choice = get_choice(["Go left (master bedroom)", "Go right (guest bedroom)"])
  if choice == 1:
    return "master_bedroom", clues
  else:
    return "guest_bedroom", clues

def room_master_bedroom(clues):
  """Handles the master bedroom logic."""
  print("\nYou enter the master bedroom, a luxurious room with a large bed and a balcony.")
  if "diary_clue" not in clues:
    print("You find a diary on the nightstand. The latest entry mentions a heated argument with the victim.")
    clues.append("diary_clue")
  else:
    print("The master bedroom seems as you left it.")
  print("There is a door leading back to the staircase.")
  choice = get_choice(["Go back to the staircase"])
  return "staircase", clues  # Return "staircase" to go back

def room_guest_bedroom(clues):
  """Handles the guest bedroom logic."""
  print("\nYou enter the guest bedroom, a cozy room with a single bed and a window overlooking the garden.")
  if "letter_clue" not in clues:
    print("You find a crumpled letter under the bed. It's a threatening letter addressed to the victim.")
    clues.append("letter_clue")
  else:
    print("The guest bedroom seems as you left it.")
  print("There is a door leading back to the staircase.")
  choice = get_choice(["Go back to the staircase"])
  return "staircase", clues  # Return "staircase" to go back

def interrogate_suspect(suspect, clues):
  """Allows the player to interrogate a suspect."""
  print(f"\nYou interrogate {suspect}.")
  if suspect == "Butler":
    print("The butler seems nervous and avoids eye contact.")
    choice = get_choice(["Ask about his whereabouts during the murder", "Ask about his relationship with the victim"])
    if choice == 1:
      print("He claims he was polishing silverware in the pantry.")
      if "wine_clue" in clues:
        print("But you remember the wine glass with the unusual lipstick stain...")
      else:
        print("He admits he had a disagreement with the victim about a missing heirloom.")
  elif suspect == "Maid":
    print("The maid is visibly upset and keeps glancing at the master bedroom.")
    choice = get_choice(["Ask about her whereabouts during the murder", "Ask about her relationship with the victim"])
    if choice == 1:
      print("She claims she was cleaning the guest bedroom.")
      if "letter_clue" in clues:
        print("But you remember the threatening letter found under the bed...")
      else:
        print("She reveals she overheard the victim arguing with someone in the garden.")
  elif suspect == "Gardener":
    print("The gardener appears aloof and uninterested in the investigation.")
    choice = get_choice(["Ask about his whereabouts during the murder", "Ask about his relationship with the victim"])
    if choice == 1:
      print("He claims he was tending to the roses in the garden.")
      if "book_clue" in clues:
        print("But you remember the letter mentioning a secret meeting in the garden...")
      else:
        print("He denies having any personal relationship with the victim.")
  return clues

def make_accusation(clues):
  """Allows the player to make an accusation."""
  print("\nBased on the clues you have gathered, who do you think is the murderer?")
  choice = get_choice(["Butler", "Maid", "Gardener"])
  if choice == 1 and "wine_clue" in clues:
    print("\nYou accuse the Butler! He confesses to the murder, revealing his motive was to steal the heirloom.")
    print("Congratulations, detective! You have solved the case!")
  elif choice == 2 and "letter_clue" in clues:
    print("\nYou accuse the Maid! She confesses to the murder, revealing her motive was revenge for being wronged by the victim.")
    print("Congratulations, detective! You have solved the case!")
  elif choice == 3 and "book_clue" in clues:
    print("\nYou accuse the Gardener! He confesses to the murder, revealing his motive was to silence the victim about a dark secret.")
    print("Congratulations, detective! You have solved the case!")
  else:
    print("\nYou accuse the wrong suspect! The real murderer escapes, and the case goes unsolved.")
    print("Game Over.")

def start_game():
  """Starts the game and handles the main game loop."""
  intro()
  player_name = create_character()
  current_room = "entrance"
  clues = []
  suspects = ["Butler", "Maid", "Gardener"]
  random.shuffle(suspects)  # Randomize the order of suspects

  while True:
    print("\n--- Current Location:", current_room.upper(), "---")  # Indicate current room
    if current_room == "entrance":
      current_room, clues = room_entrance(clues)
    elif current_room == "library":
      current_room, clues = room_library(clues)
    elif current_room == "dining_room":
      current_room, clues = room_dining_room(clues)
    elif current_room == "staircase":
      current_room, clues = room_staircase(clues)
    elif current_room == "master_bedroom":
      current_room, clues = room_master_bedroom(clues)
    elif current_room == "guest_bedroom":
      current_room, clues = room_guest_bedroom(clues)

    # Interrogation phase after visiting all rooms
    if len(clues) >= 3:  # Corrected condition
      print("\nYou've explored the mansion. Time to interrogate the suspects!")
      for suspect in suspects:
        clues = interrogate_suspect(suspect, clues)  # Update clues after each interrogation
      make_accusation(clues)
      break

if __name__ == "__main__":
  start_game()