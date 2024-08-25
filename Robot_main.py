from Houses import Cave
from new_game_characters import Enemy  # Corrected import statement

# Create house instances
cedar_ridge = Cave('Cedar Ridge')
cedar_ridge.set_description("A serene house with a view of the surrounding forest.")

willow_cottage = Cave('Willow Cottage')
iron_gate = Cave('Iron Gate')
iron_gate.set_description("A grand house with a collection of old relics.")
willow_cottage.set_description("A charming house with ivy-covered walls.")

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

# Set the current house
current_house = cedar_ridge

# Game loop
while True:
    current_house.get_details()  # Show the player the details of the current house
    inhabitant = current_house.get_character()  # Check if there's a character in the house

    if inhabitant:
        print("There is a " + inhabitant.name + " here.")
        print(inhabitant.description)
        action = input("Do you want to talk, fight or escape?").strip().lower()

        if action == "talk":
            inhabitant.talk()
        elif action == "fight":
            combat_item = input("What will you use to fight? ").strip()
            if not inhabitant.fight(combat_item):
                print("Game Over!")
                break
        else:
            print("You don't do anything.")
    else:
        command = input("Which direction? (north, south, east, west) ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            current_house = current_house.move(command)  # Move to the linked house
        else:
            print("Invalid direction. Try again.")
