import random
# dávej run v dogs.py ne v Dog.py #
class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Vytvářím objekt psa s jménem {self.name}.")

    def bark(self):
        print(self.name + " štěká!")

    def hp(self):
        print(self.name + " má " + str(random.randint(75, 150)) + " životů.")