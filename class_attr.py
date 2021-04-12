
###################
# Attributes
###################

# The syntax for creating an attribute is:
#
#     self.attribute = something
#
# There is a special method called:
#
#     __init__()
#
# This method is used to initialize the attributes of an object. For example:


class Dog():
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

lotta = Dog(breed='Labrador Retriever', name="Milly")

zee = Dog('Huskie', 'Morris')
