class Animal:
    def sound(self):
        print("Animals have their own sounds...")


class Dog(Animal):
    def sound(self):
        print("Gheu Gheu!!")


common = Animal()
doggo = Dog()

common.sound()
doggo.sound()
