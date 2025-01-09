'''

Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common parent class, and methods to behave differently based on the object.

'''
class Shape:
    def area(self):
        """Placeholder method for calculating area."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# List of shapes
shapes = [Circle(5), Rectangle(4, 6)]

# Calculate area of all shapes
for shape in shapes:
    print(f"Area: {shape.area()}")
# Output:
# Area: 78.5
# Area: 24