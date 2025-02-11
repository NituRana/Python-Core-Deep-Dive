'''

Abstraction hides the internal details and shows only the essential features. In Python, abstraction can be achieved 
using abstract base classes (ABC module).

'''

from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """Abstract method to be implemented by subclasses."""
        pass

# Subclass implementing the abstract method
class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick.")

# Create objects and call the implemented method
car = Car()
bike = Bike()
car.start()  # Output: Car starts with a key.
bike.start()  # Output: Bike starts with a kick.