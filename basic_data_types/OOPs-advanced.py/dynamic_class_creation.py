# --------------------------------------
# 6. Dynamic Class Creation
# --------------------------------------
def create_class(class_name, base_classes, attributes):
    """Dynamically creates a class."""
    return type(class_name, base_classes, attributes)

# Dynamically create a class
DynamicClass = create_class(
    "DynamicClass",
    (object,),  # Base classes
    {"greet": lambda self: "Hello, I'm a dynamic class"}  # Attributes
)

# Example usage:
dynamic_instance = DynamicClass()
print(dynamic_instance.greet())  # Output: Hello, I'm a dynamic class