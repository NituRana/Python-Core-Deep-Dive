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


#==========================================================================================================
#----------------------------------------- Common Dictionary Methods -------------------------------------
#==========================================================================================================

# |Method	             |  Description	                                           |  Example
# |get(key[, default])	 |  Returns the value for the key; default if missing	   |  d.get("key", "default")
# |keys()	             |  Returns a view object of keys	                       |  d.keys()
# |values()	             |  Returns a view object of values	                       |  d.values()
# |items()	             |  Returns a view object of key-value pairs	           |  d.items()
# |update(other_dict)	 |  Updates the dictionary with key-value pairs	           |  d.update({"key": "value"})
# |pop(key[, default])	 |  Removes a key and returns its value	                   |  d.pop("key", "default")
# |clear()	             |  Removes all entries	                                   |  d.clear()

#==========================================================================================================
#--------------------------------------- Applications of Dictionaries -------------------------------------
#==========================================================================================================

# 1. Lookup Tables
# Dictionaries are excellent for mapping keys to values.

# Example: Employee details
employees = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}
print(employees[102])  # Output: Bob
#-------------------------------------------------------------------------------------------------------------------

# 2. Counting Frequencies
# Count the occurrences of items in a list.

words = ["apple", "banana", "apple", "cherry", "banana", "banana"]

# Count frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)  # Output: {'apple': 2, 'banana': 3, 'cherry': 1}
#-------------------------------------------------------------------------------------------------------------------

# 3. Caching
# Store computed results to avoid redundant calculations.

# Example: Caching Fibonacci numbers
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        return n
    fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_cache[n]

print(fibonacci(10))  # Output: 55

#==========================================================================================================
#--------------------------------------- Advanced Features ------------------------------------------------
#==========================================================================================================

# 1. Nested Dictionaries
# Dictionaries can hold other dictionaries.

# Nested structure for student data
students = {
    "101": {"name": "Alice", "age": 21},
    "102": {"name": "Bob", "age": 22}
}
print(students["101"]["name"])  # Output: Alice

#------------------------------------------------------------------------------------------------------------

# 2. Dictionary Comprehensions
# Create dictionaries with concise syntax.

# Square numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#--------------------------------------------------------------------------------------------------------------

# 3. Default Dictionaries
# Use collections.defaultdict for automatic default values.

from collections import defaultdict

# Default dictionary with int
freq = defaultdict(int)
words = ["apple", "banana", "apple"]
for word in words:
    freq[word] += 1
print(freq)  # Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})
#--------------------------------------------------------------------------------------------------------------
# Performance Considerations

# Dictionaries have average O(1) complexity for lookups, additions, and deletions.
# However, their memory usage is higher than lists because of the underlying hash table.
#--------------------------------------------------------------------------------------------------------------