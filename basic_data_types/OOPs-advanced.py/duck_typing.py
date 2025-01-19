# --------------------------------------
# 3. Duck Typing
# --------------------------------------
class Bird:
    """Duck typing example."""
    def fly(self):
        return "Bird is flying."

class Airplane:
    def fly(self):
        return "Airplane is flying."

class Fish:
    def swim(self):
        return "Fish is swimming."

def let_it_fly(obj):
    """Duck typing: checks if obj can fly."""
    return obj.fly()

# Example usage:
bird = Bird()
airplane = Airplane()
print(let_it_fly(bird))       # Output: Bird is flying.
print(let_it_fly(airplane))   # Output: Airplane is flying.
# let_it_fly(Fish())  # Will raise an AttributeError