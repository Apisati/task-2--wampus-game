class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


#enemy class code here
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)  # call the constructor of the superclass
        self.weakness = None

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, item):
        # item is a string value that weakens the enemy
        self.weakness = item

    def fight(self, combat_item):
        def fight(self, combat_item):
            if combat_item == self.weakness:
                print("You fend " + self.name + " off with the " + combat_item)
                return True
            else:
                print(self.name + " swallows you, little wimp")
                return False
