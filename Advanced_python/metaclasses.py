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