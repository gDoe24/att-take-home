

class Animal:
    
    dogs = 0
    cats = 0
    sheeps = 0

    @classmethod
    def _update_amount(cls, species):

        if species == "sheep":
            cls.sheeps += 1
        elif species == "dog":
            cls.dogs += 1
        elif species == "cat":
            cls.cats += 1


    def __init__(self, name, color, species, birthday):
        self.name = name
        self.color = color
        self.species = species
        self.birthday = birthday
        Animal._update_amount(species)
    

    pass

class Dog(Animal):
    
    def make_sound(self, name, color):
        return f"{name} the {color} dog says bark"

class Cat(Animal):

    def make_sound(self, name, color):
        return f"{name} the {color} cat says meow"

class Sheep(Animal):

    def make_sound(self, name, color):
        return f"{name} the {color} sheep says baa"


