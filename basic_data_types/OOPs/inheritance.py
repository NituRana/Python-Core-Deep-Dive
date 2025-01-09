'''

Inheritance allows a class (child) to inherit properties and methods from another class (parent), promoting code reuse.

'''

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create objects of child classes
dog = Dog("Buddy")
cat = Cat("Kitty")

# Call the overridden methods
dog.speak()  # Output: Buddy says Woof!
cat.speak()  # Output: Kitty says Meow!
