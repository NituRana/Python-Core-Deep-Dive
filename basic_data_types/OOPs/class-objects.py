'''
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data in the form 
of attributes (also called properties) and code in the form of methods (functions that operate on the data). Python is an 
object-oriented language, making it easy to implement OOP concepts.
'''

# 1. Class and Object
# A class is a blueprint for creating objects. An object is an instance of a class.


# Define a class (blueprint for objects)
class Dog:
    # Constructor to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute: name of the dog
        self.breed = breed  # Attribute: breed of the dog
    
    # Method to display dog details
    def display_info(self):
        print(f"My name is {self.name} and I am a {self.breed}.")

# Create an object (instance of Dog class)
dog1 = Dog("Buddy", "Golden Retriever")

# Call the method using the object
dog1.display_info()  # Output: My name is Buddy and I am a Golden Retriever.