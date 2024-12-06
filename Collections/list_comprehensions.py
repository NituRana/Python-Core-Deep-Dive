#==========================================================================================================
#------------------------------------------- List Comprehension -------------------------------------------
#==========================================================================================================

'''

1. What is List Comprehension?
List comprehension is a syntactic construct for creating lists based on existing iterables. It allows
the application of transformations and filters to iterables in a single, compact line of code.

Syntax:

[expression for item in iterable if condition]

Expression: Operation or transformation to apply to each item.
Iterable: The sequence to iterate over (e.g., list, tuple, range, or string).
Condition (optional): A filtering condition to decide which items are included.

'''
#------------------------------------- Basics of List Comprehension ------------------------------------------

# a. Simple Iteration
# Create a list from another iterable:

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
#-------------------------------------------------------------------------

# b. Filtering with Conditions
# Add an if clause to include only certain elements:


numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]
#-------------------------------------------------------------------------

# c. Transformation with Filtering
# Combine transformation and filtering:

numbers = [1, 2, 3, 4, 5]
transformed = [x * 2 for x in numbers if x > 2]
print(transformed)  # Output: [6, 8, 10]
#-------------------------------------------------------------------------------------------------------------------

#----------------------------------- Advanced List Comprehension ---------------------------------------------------

# a. Nested Loops
# You can use multiple for loops inside a list comprehension. This is useful for flattening nested iterables or creating
# combinations.

# Flattening a 2D List:


matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for row in matrix for item in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
#-------------------------------------------------------------------------

# Creating Cartesian Products:

colors = ['red', 'blue']
sizes = ['S', 'M']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)  # Output: [('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]
#-------------------------------------------------------------------------

# b. Conditional Expressions in Transformation
# Include conditional logic in the transformation:

numbers = [1, 2, 3, 4, 5]
transformed = [x ** 2 if x % 2 == 0 else x ** 3 for x in numbers]
print(transformed)  # Output: [1, 4, 27, 16, 125]
#-------------------------------------------------------------------------

# c. Nested List Comprehension
# Handle complex nested structures:

# Transpose a matrix using nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#-------------------------------------------------------------------------

# d. Using Functions Inside List Comprehension
# Call external or lambda functions for transformations:


def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = [square(x) for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
#-------------------------------------------------------------------------

# e. Set and Dictionary Comprehensions
# List comprehension isn't limited to lists; you can create sets and dictionaries in a similar way.

# Set Comprehension:

numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # Output: {16, 1, 4, 9}
#-------------------------------------------------------------------------

# Dictionary Comprehension:


words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
print(lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Real-World Applications ----------------------------------------------------


# a. Data Cleaning
# List comprehensions are often used to clean or process datasets.

# Example: Removing Extra Spaces

data = ["  apple", "banana  ", "  cherry  "]
cleaned_data = [item.strip() for item in data]
print(cleaned_data)  # Output: ['apple', 'banana', 'cherry']
#-------------------------------------------------------------------------

# b. Extracting Specific Data
# Filter or extract relevant data from collections.

# Example: Extracting Usernames

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]
usernames = [user["name"] for user in users]
print(usernames)  # Output: ['Alice', 'Bob', 'Charlie']
#-------------------------------------------------------------------------


# c. Performance Improvement
# List comprehensions are faster than traditional loops in most cases.

# Example: Comparing Performance

import timeit

# Using list comprehension
list_comp_time = timeit.timeit("[x ** 2 for x in range(1000)]", number=10000)

# Using loop
loop_time = timeit.timeit("""
result = []
for x in range(1000):
    result.append(x ** 2)
""", number=10000)

print(f"List Comprehension: {list_comp_time}, Loop: {loop_time}")
# Output: List Comprehension is significantly faster

#-------------------------------------------------------------------------
# d. Data Transformation in Files
# Transform or filter data from files using list comprehension.

# Example: Reading Only Error Logs

logs = [
    "INFO: All systems operational",
    "ERROR: Disk full",
    "WARNING: High memory usage",
    "ERROR: Network timeout"
]
error_logs = [log for log in logs if log.startswith("ERROR")]
print(error_logs)  # Output: ['ERROR: Disk full', 'ERROR: Network timeout']