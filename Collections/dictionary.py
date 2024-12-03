#==========================================================================================================
#----------------------------------------- Dictionaries in Python ----------------------------------------
#==========================================================================================================


'''
What is a Dictionary?
A dictionary in Python is an unordered collection of key-value pairs, where:

1. Keys: Must be unique and immutable (strings, numbers, tuples, etc.).
2. Values: Can be any data type and are not required to be unique.
3. Dictionaries are optimized for fast lookups, additions, and deletions based on keys.

'''
#----------------------------------------------------- Key Properties ---------------------------------------------
# 1. Creating a Dictionary

empty_dict = {}

student = {"name": "John", "age": 21, "grade": "A"}
print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

# Using dict() constructor
employee = dict(id=101, name="Alice", salary=50000)
print(employee)  # Output: {'id': 101, 'name': 'Alice', 'salary': 50000}
#-------------------------------------------------------------------------------------------------------------------

# 2. Accessing Values
# Use the key to access its associated value.


student = {"name": "John", "age": 21}

# Access using key
print(student["name"])  # Output: John

# Using get() (returns None if the key does not exist)
print(student.get("grade"))  # Output: None

#-------------------------------------------------------------------------------------------------------------------

# 3. Adding and Modifying Entries

student["grade"] = "A"
print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

# Modifying an existing key-value pair
student["age"] = 22
print(student)  # Output: {'name': 'John', 'age': 22, 'grade': 'A'}