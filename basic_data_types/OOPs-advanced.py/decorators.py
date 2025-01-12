# --------------------------------------
# 1. Decorators and Static/Class Methods
# --------------------------------------

class MyClass:
    """Demonstrates static and class methods with decorators."""
    
    factor = 10  # Class-level attribute
    
    @staticmethod
    def static_method(x):
        """Static method: Doesn't access class or instance state."""
        return x * x

    @classmethod
    def class_method(cls, x):
        """Class method: Can access class-level attributes."""
        return x * cls.factor

# Example usage:
print(MyClass.static_method(5))  # Output: 25
print(MyClass.class_method(5))   # Output: 50