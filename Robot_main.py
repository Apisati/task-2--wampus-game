from Houses import Cave
from new_game_characters import Enemy  # Corrected import statement

# Create house instances
cedar_ridge = Cave('Cedar Ridge')
cedar_ridge.set_description("A serene house with a view of the surrounding forest.")

willow_cottage = Cave('Willow Cottage')
iron_gate = Cave('Iron Gate')
iron_gate.set_description("A grand house with a collection of old relics.")
willow_cottage.set_description("A charming house with ivy-covered walls.")

# Set weapons
iron_gate.set_weapon('Water')

# Link houses
iron_gate.link_cave(willow_cottage, "west")
iron_gate.link_cave(cedar_ridge, "north")
cedar_ridge.link_cave(iron_gate, "south")
willow_cottage.link_cave(iron_gate, "east")

# Create and configure Enemy instance
robot = Enemy("Robot#2347", "A rigid bot with metal plating and glowing eyes.")
robot.set_conversation("Hello.. time to die")
robot.set_weakness("Water")

# Place the robot in Cedar Ridge
cedar_ridge.set_character(robot)

# Place items in houses
iron_gate.item = "Water"  # An item to defeat the robot
willow_cottage.item = "Torch"  # A random item (not useful against the robot)

# Set the current house
current_house = cedar_ridge

# Player's inventory
inventory = []

# Game loop
while True:
    current_house.get_details()  # Show the player the details of the current house
    inhabitant = current_house.get_character()  # Check if there's a character in the house

    # Check for items in the current house
    if current_house.get_weapon() is not None:
        print(f"You found a {current_house.item}!")
        take_item = input(f"Do you want to take the {current_house.item}? (yes/no) ").strip().lower()
        if take_item == "yes":
            inventory.append(current_house.item)
            print(f"{current_house.item} added to your inventory.")
            current_house.item = None  # Remove the item from the house

    if inhabitant:
        print("There is a " + inhabitant.name + " here.")
        print(inhabitant.description)
        action = input("Do you want to talk, fight, or escape? ").strip().lower()

        if action == "talk":
            inhabitant.talk()
        elif action == "fight":
            print(f"Your inventory: {inventory}")
            combat_item = input("What will you use to fight? ").strip()
            if combat_item in inventory:
                if not inhabitant.fight(combat_item):
                    print("Game Over!")
                    break
            else:
                print("You don't have that item.")
        elif action == "escape":
            print("You manage to escape and find yourself back at the entrance.")
            current_house = iron_gate  # Move to a different house after escaping
        else:
            print("You don't do anything.")
    else:
        command = input("Which direction? (north, south, east, west) ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            current_house = current_house.move(command)  # Move to the linked house
        else:
            print("Invalid direction. Try again.")
