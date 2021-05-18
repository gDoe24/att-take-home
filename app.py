from datetime import datetime

'''
Animal class initializes the name, color and birthday
Use a method to set the most_common animal species to the
        respective species' class
Keeps an array of available species have been instantiated from Animal
Holds static methods for formatting bithday and turning species from string
    to class object
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

    @staticmethod
    def format_birthday(birthday):
        try:
            birthday = datetime.strptime(birthday, "%m/%d/%Y")
            return birthday
        except ValueError:
            raise ValueError

    @staticmethod
    def get_species(species):

        if species.lower() == "dog":
            species = Dog
        elif species.lower() == "cat":
            species = Cat
        elif species.lower() == "sheep":
            species = Sheep
        else:
            raise TypeError
        return species


'''
Species concrete classes keep track of their count, their oldest animal,
    and makes its own sound
Each species adds itself to the Animal available_species class object
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
        return f"{oldest.name}, the {oldest.color} dog says bark!"


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
        return f"{oldest.name}, the {oldest.color} cat says meow!"


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
        return f"{oldest.name}, the {oldest.color} sheep says baa!"


'''
add animals loops through a prompt asking for the animal input until
    the user specifies not to
'''


def add_animals():

    active = True
    while active:
        animal = input("Please input your animal: ")
        animal_arr = animal.split(",")
        name = animal_arr[0]
        color = animal_arr[1]
        species = animal_arr[2]
        animal_birthday = animal_arr[3]

        try:
            species = Animal.get_species(species)
        except TypeError:
            print("Enter a valid species")
            continue

        try:
            birthday = Animal.format_birthday(animal_birthday)
        except ValueError:
            print(f"Please check birthday format for {name}")
            continue

        species(name=name, color=color, birthday=birthday)

        cont = input("Continue with more animals? (Y/N): ")
        if cont.lower() == "y":
            continue
        else:
            active = False

    most_common = Animal.set_most_common()
    print(most_common.make_sound())
