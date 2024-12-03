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

#-------------------------------------------------------------------------------------------------------------------
# 4. Deleting Entries

del student["grade"]
print(student)  # Output: {'name': 'John', 'age': 22}

# Using pop() (returns the removed value)
age = student.pop("age")
print(age)       # Output: 22
print(student)   # Output: {'name': 'John'}

# Removing all entries
student.clear()
print(student)  # Output: {}

#-------------------------------------------------------------------------------------------------------------------

# 5. Iterating Over a Dictionary

student = {"name": "John", "age": 21, "grade": "A"}

# Iterate over keys
for key in student:
    print(key)  # Output: name, age, grade

# Iterate over values
for value in student.values():
    print(value)  # Output: John, 21, A

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 21
# grade: A

#-------------------------------------------------------------------------------------------------------------------
