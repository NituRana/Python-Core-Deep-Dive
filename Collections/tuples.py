#==========================================================================================================
#-------------------------------------------- Tuples in Python ---------------------------------------
#==========================================================================================================
'''
What is a Tuple?
    Definition: A tuple is an ordered, immutable, and iterable collection in Python.

Key Properties:
    1. Ordered: Elements maintain the order in which they were added.
    2. Immutable: Once created, elements cannot be changed, added, or removed.
    3. Heterogeneous: Can contain elements of different data types.
    4. Hashable: Tuples can be used as keys in dictionaries if all elements within the tuple are hashable.
'''

#---------------------------------------------- Creating a Tuple -------------------------------------------

# 1. Creating a Tuple
# Tuples are defined using parentheses () or the tuple() constructor.

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Single element tuple
single_element = (42,)
print(single_element)  # Output: (42,)

# Homogeneous tuple
numbers = (1, 2, 3)
print(numbers)  # Output: (1, 2, 3)

# Heterogeneous tuple
mixed = ("apple", 3.14, True)
print(mixed)  # Output: ('apple', 3.14, True)

#---------------------------------------------- Accessing Elements -------------------------------------------

# 2. Accessing Elements
# Tuples support indexing and slicing, similar to lists.

fruits = ("apple", "banana", "cherry")

# Access by index
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry

# Slicing
print(fruits[1:])  # Output: ('banana', 'cherry')

#---------------------------------------------- Tuple Immutability -------------------------------------------
# 3. Tuple Immutability
# Once created, you cannot modify a tuple’s content.

numbers = (1, 2, 3)

# Attempt to modify (raises an error)
# numbers[0] = 42  # TypeError: 'tuple' object does not support item assignment

# However, if a tuple contains a mutable element (e.g., a list), the mutable element itself can be modified.

nested = (1, [2, 3], 4)
nested[1][0] = 42
print(nested)  # Output: (1, [42, 3], 4)

#==========================================================================================================
#----------------------------------------------  When to Use Tuples ----------------------------------------
#==========================================================================================================

#---------------------------------------------- 1. Fixed Collections -------------------------------------------
# 1. Fixed Collections
# Tuples are ideal for representing collections of data that should not change, such as coordinates, RGB colors, or configurations.

# Coordinates
point = (3, 4)
print(f"X: {point[0]}, Y: {point[1]}")  # Output: X: 3, Y: 4

#---------------------------------------------- 2. Keys in Dictionaries -------------------------------------------
# 2. Keys in Dictionaries
# Because tuples are immutable and hashable, they can serve as keys in dictionaries.
# Dictionary with tuple keys
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
}
print(locations[(40.7128, -74.0060)])  # Output: New York

#---------------------------------------- Returning Multiple Values from a Function ---------------------------------

# 3. Returning Multiple Values from a Function
# Tuples are commonly used to return multiple values from a function.

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([1, 2, 3, 4])
print(result)  # Output: (1, 4)

# Unpacking the tuple
minimum, maximum = result
print(minimum, maximum)  # Output: 1 4
#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------

#---------------------------------------------- Key Operations -------------------------------------------


