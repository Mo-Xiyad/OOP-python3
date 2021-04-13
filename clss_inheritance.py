# INHERITANCE

#classOne
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

#inheriting from classOne .Animal
class Bird(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Bird Created")

    def bark(self):
        print('Woof Woof Woof')

    def eat(self):
        print('Bird Eating')


 mya = Bird()
 mya.whoAmI()
 mya.eat()
 mya.bark()
