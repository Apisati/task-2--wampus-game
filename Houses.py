class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.weapon = None

    def get_character(self):
        return self.character

    def set_character(self, character):
        self.character = character

    def get_description(self):
        return self.description

    def set_description(self, cave_description):
        self.description = cave_description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, cave_name):
        self.name = cave_name

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
            print("The " + cave.get_name() + " is " + direction)

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon
