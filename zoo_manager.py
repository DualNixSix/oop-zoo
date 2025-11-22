class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def __str__(self):
        return f"{self.name}"
    
    def speak(self):
        print (f"\nI am a {self.species} and I make the {self.sound}.")
    
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, species="Mammal", sound="Generic Mammal Sound")
    
    def give_birth(self):
        print (f"\n{self} has given birth!")

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name, species="Bird", sound="Generic Bird Sound")
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name, species="Reptile", sound="Generic Reptile Sound") 

    def bask_in_sun(self):
        print (f"\n{self} is basking in the sun!")


# Mammal Subclasses
class Primate(Mammal):
    def __init__(self, name, sound="Primate Sound"):
        super().__init__(name)
        self.sound = sound

    def climb_trees(self):
        print (f"\n{self} is climbing trees!")

class Marsupial(Mammal):
    def __init__(self, name, sound="Marsupial Sound"):
        super().__init__(name)
        self.sound = sound

    def carry_baby(self):
        print (f"\n{self} is carrying it's baby!")
    


mammal1 = Mammal("Mr. Magoo")
bird1 = Bird("Birdy Bird", 3.0)
reptile1 = Reptile("Raphael")
primate1 = Primate("Privyet")
marsupial1 = Marsupial("Mrs. Magoo")


# ## Part 3: Zoo Attractions

# class Aviary:
#     def __init__(self, birds):
#         self.birds = birds

# class ReptileEnclosure:
#     def __init__(self, reptiles):
#         self.reptiles = reptiles
       
        
mammal1.give_birth()
print (f"\n{bird1.name}'s wingspan is {bird1.wingspan} meters long!")
reptile1.bask_in_sun()
primate1.climb_trees()
marsupial1.carry_baby()
mammal1.speak()
reptile1.speak()
primate1.speak()
marsupial1.speak()