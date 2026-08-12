# Valhalla - developed by Bruce Hoiberg
# A text based adventure game
# Last update 8/10/2026

def move(command_text: str,
         room: str,
         rooms_map: dict,
         pack: dict):
    """
    This function controls the movement of the valhalla game. It returns the current room
    :param command_text: Movement command enter by user
    :param room: Current room
    :param rooms_map: Dictionary of the rooms map with the rooms name, movement directions, and new room in that direction
    :param pack: Dictionary of the pack items with a mystical item and a boolean value that controls if the user has picked up the item
    :return: room: str
    """

    if command_text in rooms_map[room]:
        room = rooms_map[room][command_text]
        rooms(room, mystical_item, pack)
    else:
        no_rooms(command_text, room)

    return room


def pack_items(pack: dict,
               my_pack: list):
    """
    This function prints out the current pack items, or empty
    :param pack: Dictionary of the pack items with a mystical item and a boolean value that controls if the user has picked up the item
    :param my_pack: List of mystical items currently in the users pack
    :return: None
    """

    count = 0
    print(f"\nYour Pack Items:")

    # See if the user has anything in their pack
    for item in pack:
        if pack[item] == True and item != "Empty" and item != "Loki":
            count += 1

    if count == 0:
        print("Your pack is empty.")
    else:
        print(my_pack)


def mystical_items(mystical_item: dict,
                   my_pack: list,
                   pack: dict,
                   room: str,
                   win: bool):
    """
    This function controls the boolean values for dictionary pack and adds items to list my_pack.
    It also sets win to True if the user has picked up all 7 of the Mystical Items
    :param mystical_item:
    :param my_pack: List of mystical items currently in the users pack
    :param pack: Dictionary of the pack items with a mystical item and a boolean value that controls if the user has picked up the item
    :param room: Current room
    :param win: Boolean of win status
    :return: pack: dict,
             my_pack: list,
             win: bool
    """

    # Variable to make if logic more readable. Contains the room string in dictionary mystical_item
    mystical = mystical_item[room][0]

    if pack[mystical] == False:
        print(f"You have picked up the Mystical Item {mystical_item[room][1]}")
        pack[mystical] = True
        my_pack.append(mystical)

        # Check if the user has picked up all 7 Mystical Items, break if it encounters a False value
        for item in pack:
            if pack[item] == False and item != "Empty":
                break
            # You have gotten thru checking all Mystical Items for False
            elif item == "Empty":
                print("\nYou have retrieved all 7 Mystical Items from Valhalla!")
                print("Now find the Evil Trickster Loki and banish him from Valhalla!\n")
                win = True

    # Semantics based on the room the user is in
    elif room in ["Odin's Bedroom", "Frigg's Bedroom"]:
        print(f"There is nothing left to pick up in {room}.")
    else:
        print(f"There is nothing left to pick up in the {room}.")

    return pack, my_pack, win

def rooms(room: str,
          mystical_item: dict,
          pack: dict):
    """
    This function prints out details about the current room you're in
    :param room: Current room
    :param mystical_item: Dictionary of the Mystical Items
    :param pack: Dictionary of the pack items with a mystical item and a boolean value that controls if the user has picked up the item
    :return: None
    """

    mystical = mystical_item[room][0]

    if pack[mystical] == False and room in ["Odin's Bedroom", "Frigg's Bedroom"]:
        print(f"\nYou are now in {room}. You look around and see {mystical_item[room][1]}")
    elif pack[mystical] == False:
        print(f"\nYou are now in the {room}. You look around and see {mystical_item[room][1]}")
    elif room == "Great Hall":
        print(f"\nYou are now in the {room}.")
    elif room == "Dungeon":
        print(f"\nYou are now in the {room}. You look around and see {mystical_item[room][1]}")
    elif pack[mystical] == True and room in ["Odin's Bedroom", "Frigg's Bedroom"]:
        print(f"\nYou are now in {room}. {room} room is now empty.")
    else:
        print(f"\nYou are now in the {room}. The {room} room is now empty.")


def no_rooms(command_text: str,
             room: str):
    """
    This function prints out there are no rooms to explore in the input direction
    :param command: String of the input command
    :param room: Current room
    :return: None
    """
    print(f"There are no rooms to explore {command_text} from room {room}. Please choose another direction.")

def status(pack: dict,
           my_pack: list,
           room: str,
           mystical_item: dict):
    """
    This function calls 2 functions that print out the current status of the user in Valhalla
    :param pack: Dictionary of the pack items with a mystical item and a boolean value that controls if the user has picked up the item
    :param my_pack: List of mystical items currently in the users pack
    :param room: Current room
    :param mystical_item: Dictionary of the Mystical Items
    :return: None
    """

    rooms(room, mystical_item, pack)
    pack_items(pack, my_pack)

def get_command(mystical_item: dict,
                pack: dict,
                commands: dict,
                rooms_map: dict,
                my_pack: list,
                win: bool,
                room: str):
    """
    This function creates the logical structure of the program
    :param mystical_item: Dictionary of the Mystical Items
    :param pack: Dictionary of the pack items and controls if the item has been found and picked up
    :param commands: Dictionary of the valid commands for input
    :param rooms_map: Dictionary of the rooms and valid directions to move from the room
    :param my_pack: List of mystical items currently in the users pack
    :param win: Boolean that controls if the users pack is full: Collected all 7 Mystical items.
    :param room: String of the current room.
    :return: pack: dict,
             my_pack: list,
             win: bool,
             room: str
    """

    direction = "N: North, S: South, E: East, W: West"
    special_commands = "C: Current Status, G: Get Mystical Item, I: Instructions, P: See Pack Items, X: Exit Program"
    print("\nPlease enter a command:")
    #print("N - North, S - South, E - East, W - West, G - Get Mystical Item", "P - See Pack Items", "X - Exit Program")
    print(f"{direction}\n{special_commands}")

    command = input().upper()

    try:
        command_text = commands[command] # Get text string from commands dictionary if it's valid
    except KeyError:
        command_text = ""

    # Check for valid direction from rooms_map dictionary
    if command in commands and command not in ("C", "G", "I", "P", "X"):
        # call move function and move to a new room if the input is valid
        room = move(command_text, room, rooms_map, pack)
    elif command == "C": # Get players current status
        status(pack, my_pack, room, mystical_item)
    elif command == "G":
        # Get item from current room, put it in the My_pack list, and set pack dictionary to True
        pack, my_pack, win = mystical_items(mystical_item, my_pack, pack, room, win)
    elif command == "I":
        game_instructions(direction, special_commands) # Display game instructions and valid user inputs
    elif command == "P":(
        pack_items(pack, my_pack)) # Show pack items
    elif command == "X":
        room = "Exit" # quit the game
    else:
        print("\nYou have entered an invalid command")

    # Return all current values back to main program loop
    return (pack, my_pack, win, room)

def game_instructions(direction, special_commands):
    """
    This function displays the game instructions and commands that the user can enter
    :param direction: Valid movement directions
    :param special_commands: Valid special commands
    :return:
    """
    print("\nValhalla Game Instructions:")
    print("Collect all 7 Mystical Items before finding Loki")
    print(f"Movement Directions: {direction}")
    print(f"Special Commands: {special_commands}")

def greeting():
    """
    This function prints out a greeting message
    :return:
    """
    print("""
        You are a legendary Elf known for your swiftness and stealth. 
        Odin has tasked you with saving the realm from the Evil Trickster, Loki. 
        Loki has taken over Valhalla and you need to retrieve the 7 mystical items in Valhalla before encountering Loki. 
        There is a Magic Feather in the secret chambers, a Ring of Power in Odin’s bedroom,
        a Cloak of Invisibility in Frigg’s bedroom, Thor’s Hammer in the weapon depot,
        a Dragon Toothed Necklace in the Dragon’s Lair, a Legendary Crown in the throne room,
        and an Ancient Scroll in the spell library. 
        With all 7 of these items, you can successfully banish Loki once and for all. 
        Be careful, because Loki is hiding in the Dungeon. If you encounter him before retrieving all 7 items, 
        he will cast a spell on you, enabling him to remain in Valhalla and doom the realm. """)

# Define the Mystical Items with room, mystical item, text for printing
mystical_item = {"Great Hall": ["Empty", "an empty Hall."],
                 "Secret Chambers": ["Magic Feather", "a Magic Feather."],
                 "Odin's Bedroom": ["Ring of Power", "a Ring of Power in Odin's Bedroom."],
                 "Frigg's Bedroom": ["Cloak of Invisibility", "a Cloak of Invisibility in Frigg's Bedroom."],
                 "Weapon Depot": ["Thor's Hammer", "Thor's Hammer."],
                 "Spell Library": ["Ancient Scroll", "an Ancient Scroll."],
                 "Dragon's Lair": ["Dragon Toothed Necklace", "a Dragon Toothed Necklace."],
                 "Throne Room": ["Legendary Crown", "a Legendary Crown."],
                 "Dungeon": ["Loki", "The Evil Trickster Loki"]}

# Define the pack with a mystical item and a boolean value that controls if the user has picked up the item
# the program can change all boolean values, except Empty for the Great Hall and Loki for the Dungeon
pack = {"Magic Feather": False, "Ring of Power": False, "Cloak of Invisibility": False, "Thor's Hammer": False,
        "Ancient Scroll": False, "Legendary Crown": False, "Dragon Toothed Necklace": False, "Empty": True, "Loki": True}


# Define the valid commands the user can input. Program uses the .upper string method so lowercase input will also work
commands = {"N": "North", "S": "South", "E": "East", "W": "West",
            "C": "Current Status", "I": "Instructions", "G": "Get Mystical Item", "P": "See Pack", "X": "Exit Program"}

# Define the map of rooms with the rooms name, movement directions, and new room in that direction
rooms_map = {"Great Hall": {"North": "Throne Room", "South": "Dragon's Lair", "East": "Weapon Depot", "West": "Odin's Bedroom"},
             "Secret Chambers": {"East": "Odin's Bedroom"},
             "Odin's Bedroom": {"North": "Frigg's Bedroom", "East": "Great Hall", "West": "Secret Chambers"},
             "Frigg's Bedroom": {"South": "Odin's Bedroom"},
             "Weapon Depot": {"East": "Spell Library", "West": "Great Hall"},
             "Spell Library": {"West": "Weapon Depot"},
             "Dragon's Lair": {"North": "Great Hall", "East": "Dungeon"},
             "Throne Room": {"South": "Great Hall"},
             "Dungeon": {}, "Exit": {}}

# set initial variable to start the game
my_pack = []
win = False
room = "Great Hall"

# Greeting message
greeting()

# Loop until the user wants to quit, or enters the Dungeon
while room not in ("Dungeon", "Exit"):
    pack, my_pack, win, room = get_command(mystical_item, pack, commands, rooms_map, my_pack, win, room)

# If the user enters the Dungeon, output the status of their game and terminate program, otherwise output they quit the game and exited
if room == "Dungeon":
    if win == True:
        print("\nCongratulations! You won the game. You have banished Loki once and for all!")
    else:
        print("\nSorry, you didn't retrieve all 7 Mystical Items.\nLoki has cast a spell on you. You’ve lost the game.")

    print("\nThank you for playing. Goodbye!")
else: #Exit
    print(f"You have exited the game. Goodbye")