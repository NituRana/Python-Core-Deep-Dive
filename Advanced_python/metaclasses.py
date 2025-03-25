'''
A metaclass is a class that defines how other classes are created. In simpler words, a metaclass is like a blueprint for classes, just as classes are blueprints for objects.

📌 Why Metaclasses?
Creating classes dynamically.
Enforcing rules or patterns across multiple classes.
Implementing complex class hierarchies.

'''

#--------------------- Creating a Simple Metaclass --------------------------
class MyMeta(type):  # Inheriting from 'type'
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with MyMeta")
        dct['greet'] = lambda self: f"Hello from {self.__class__.__name__}"
        return super().__new__(cls, name, bases, dct)
#----------------------------------------------------------------------------


#---------------------------- Using the Metaclass -----------------------------

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.greet())  # Output: Hello from MyClass

#------------------------------------------------------------------------------

#  2. Introspection

'''
Introspection is the ability to examine objects at runtime.
It involves using functions like type(), isinstance(), hasattr(), dir(), etc.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello!")

#------------------------------------------------------------------------------
# Checking attributes and methods
dog = Animal("Buddy")
print(type(dog))  # <class '__main__.Animal'>
print(isinstance(dog, Animal))  # True
print(hasattr(dog, 'name'))  # True
print(dir(dog))  # Lists all attributes and methods of 'dog'

#------------------------------------------------------------------------------
