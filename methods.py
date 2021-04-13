# CREATING CLASS METHODS ############  Methods are functions defined inside the body of a class

#Easiest way to explain is this.

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle()

# myc.radius = 33

myc.set_radius(99)

# print(myc.radius)
# print(myc.area())
