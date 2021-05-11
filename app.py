from datetime import datetime

class Animal:
    
    def __init__(self, name, color, birthday):
        self.birthday = datetime.strptime(birthday, "%m, %d, %Y")
        self.name = name
        self.color = color

    
    @classmethod
    def set_most_common(cls):
        cls.available_species = {
            Dog
        }
        cls.most_common = None
        
        for species in cls.available_species:
            if cls.most_common is None or species.get_count() > cls.most_common.get_count():
                cls.most_common = species
        return cls.most_common
        
    @classmethod
    def reset_animals(cls):
        for species in cls.available_species:
            species.reset()
        

class Dog(Animal):

    count = 0
    oldest = None
    
    def __init__(self, name, color, birthday):
        super().__init__(name, color, birthday)
        if not birthday:
            raise Exception()
        else:
            if Dog.oldest is None or self.birthday < Dog.oldest.birthday:
                Dog.oldest = self
            Dog.count += 1
    
    @classmethod
    def get_oldest(cls):
        return cls.oldest
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def make_sound(cls):
        oldest = cls.oldest
        return f"{oldest.name} the {oldest.color} dog says bark"
    
    @classmethod
    def reset(cls):
        cls.count = 0
        cls.oldest = None


