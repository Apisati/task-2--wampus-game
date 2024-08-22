class Cave:
    def __init__(self, cave_name): #constructor
            self.name = cave_name
            self.description = None
            self.linked_caves = {} #creates an e,pty dictionairy
            self.character = None


    def get_character(self):
        return self.character

    #method to set the description of cave
    def set_character(self):self, character):
        self.description = cave_character

#to get Description of cave
    def get_character(self):
        return self.character

    #method to set the description of cave
    def set_description(self, cave_description):
        self.description = cave_description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, Cavename):
        self.name = Cavename


    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self


    def get_details(self):
        self.describe()
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.get_name() + " is " + direction)


    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        # add the character attribute here
        self.character = None