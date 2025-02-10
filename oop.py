import random

class Character:
    #class attributes
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Flying", "Invisibility", "Teleportation", "Super Strength"]
    eye_colors = ["Hazel", "Blue", "Brown", "Grey"]

    #Constructor
    def __init__(self):
        self.generate_character()

    #This is a method
    def generate_character(self):
        self.hair_color = random.choice(Character.hair_colors)
        self.size = random.choice(Character.sizes)
        self.special_power = random.choice(Character.special_powers)
        self.eye_color = random.choice(Character.eye_colors)
        self.description = (
            f"Your character has {self.hair_color} hair, " 
            f"is {self.size} in size, has the power of {self.special_power},"
            f"and has {self.eye_color} eyes"
        ) 

    def __str__(self):
        return self.description

char1 = Character()
char2 = Character()

print(char1)
print(char2)