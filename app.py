  
from datetime import datetime

'''
Animal class initializes the name, color and birthday
Use a method to set the most_common animal species to the 
        respective species' class
'''
class Animal:

    available_species = []
    total = 0

    def __init__(self, name, color, birthday):
        self.birthday = birthday
        self.name = name
        self.color = color

    @classmethod
    def set_most_common(cls):

        cls.most_common = None

        for species in cls.available_species:

            species_count = species.get_count()

            if cls.most_common is None or species_count > cls.most_common.get_count():
                cls.most_common = species

        return cls.most_common
    
    @classmethod
    def set_available_species(cls, species):
        cls.available_species.append(species)


'''
Species concrete classes keep track of their count, their oldest animal,
and makes its own sound
'''
class Dog(Animal):
    
    count = 0
    oldest = None

    def __init__(self, name, color, birthday):
        super().__init__(name, color, birthday)
        
        if Dog.oldest is None or self.birthday < Dog.oldest.birthday:
            Dog.oldest = self

        if Dog not in Animal.available_species:
            Animal.set_available_species(Dog)

        Dog.count += 1
        Animal.total += 1

    @classmethod
    def get_oldest(cls):
        return cls.oldest

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def make_sound(cls):
        oldest = cls.oldest
        return f"{oldest.name}, the {oldest.color} dog says bark"


class Cat(Animal):

    count = 0
    oldest = None

    def __init__(self, name, color, birthday):
        super().__init__(name, color, birthday)
        
        if Cat.oldest is None or self.birthday < Cat.oldest.birthday:
            Cat.oldest = self
        if Cat not in Animal.available_species:
            Animal.set_available_species(Cat)
    
        Cat.count += 1
        Animal.total += 1

    @classmethod
    def get_oldest(cls):
        return cls.oldest

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def make_sound(cls):
        oldest = cls.oldest
        return f"{oldest.name}, the {oldest.color} cat says meow"


class Sheep(Animal):

    count = 0
    oldest = None

    def __init__(self, name, color, birthday):
        super().__init__(name, color, birthday)
        
        if Sheep.oldest is None or self.birthday < Sheep.oldest.birthday:
            Sheep.oldest = self
        if Sheep not in Animal.available_species:
            Animal.set_available_species(Sheep)

        Sheep.count += 1
        Animal.total += 1

    @classmethod
    def get_oldest(cls):
        return cls.oldest

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def make_sound(cls):
        oldest = cls.oldest
        return f"{oldest.name}, the {oldest.color} sheep says baa"


def add_animals(animals):

    if len(animals) == 0:
        print("Please input at least one valid animal")

    for animal in animals:        
        name = animal.get("name", None)
        color = animal.get("color", None)
        species = animal.get("species", None)
        animal_birthday = animal.get("birthday", None)
        try:
            birthday = datetime.strptime(animal_birthday, "%m, %d, %Y")
        except ValueError:
            print(f"Please check birthday format for {name}")
            continue

        species(name=name, color=color, birthday=birthday)
  
    most_common = Animal.set_most_common()
    print(most_common.make_sound())
