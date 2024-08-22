from Cave import Cave
from character import Enemy
cavern = Cave('Cavern')
cavern.set_description("A dank and dirty cave ")
grotto =Cave('Grotto')
dungeon = Cave('Dungeon')
dungeon.set_description("A large cave with a rack")
grotto.set_description("A small cave with ancient graffiti")

dungeon.link_cave(grotto,"west")
dungeon.link_cave(cavern,"north")
cavern.link_cave(dungeon,"south")
grotto.link_cave(dungeon,"east")

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")




cavern.set_description("A cavern, a moist and dark space")


current_cave = cavern  # sets the current cave

while True:
    current_cave.get_details()    #show the player the details of the current cave
    command = input("> ")    #get the player's command e.g. south
    current_cave = current_cave.move(command) #move returns a valid linked cave or self if no cave exists in the direction entered

from character import Enemy
