#---------------------------------------------------------------------------------------------------------------------
# ====================================================== 1. map() ====================================================
# The map() function is used to apply a function to each item in an iterable (like a list, tuple, or set) and returns a new iterable (of type map).


# map(function, iterable, *iterables)

'''
function: A function that specifies the operation to be applied.
iterable: One or more iterable objects.

Key Points
The function can be a regular function or a lambda.
If multiple iterables are passed, the function must accept as many arguments as there are iterables.
'''

# Examples
# Basic Example
# Applying a function to square numbers:


nums = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, nums)
print(list(squared))  # Output: [1, 4, 9, 16]

# Multiple Iterables
# Summing corresponding elements of two lists:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # Output: [5, 7, 9]

# Practical Application
# Converting a list of strings to uppercase:

names = ["alice", "bob", "charlie"]
upper_names = map(str.upper, names)
print(list(upper_names))  # Output: ['ALICE', 'BOB', 'CHARLIE']

#---------------------------------------------------------------------------------------------------------------------
# =================================================== 2. filter() ====================================================

# The filter() function is used to filter elements from an iterable based on a condition specified in a function. It returns an iterable containing only the elements for which the function evaluates to True.

'''
Syntax

filter(function, iterable)
'''
'''
function: A function that returns True or False.
iterable: The iterable to be filtered.
Key Points
The function should return a boolean value.
Only elements for which the function returns True are included in the result.
'''

# Filtering even numbers:


nums = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # Output: [2, 4, 6]

# Filtering Strings
# Filtering names with length greater than 3:

names = ["Bob", "Alice", "Eve", "Charlie"]
long_names = filter(lambda name: len(name) > 3, names)
print(list(long_names))  # Output: ['Alice', 'Charlie']

# Practical Application
# Filtering out None values:

data = [0, None, "Hello", "", 42]
valid_data = filter(None, data)  # None acts as a truthiness filter
print(list(valid_data))  # Output: ['Hello', 42]

#---------------------------------------------------------------------------------------------------------------------
# 3. reduce()
# The reduce() function, part of the functools module, is used to apply a function cumulatively to the items of an iterable, reducing it to a single value.

# Syntax

'''
from functools import reduce
reduce(function, iterable, initializer=None)
function: A function that takes two arguments and returns a single value.
iterable: The iterable to be reduced.
initializer: (Optional) Initial value to start the reduction.

Key Points
The function must accept two arguments: the accumulated value and the next element in the iterable.
Reduction proceeds left to right.
Examples
Basic Example
Finding the product of all elements:
'''

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24


# With an Initializer
# Concatenating strings with an initializer:


words = ["hello", "world", "python"]
sentence = reduce(lambda x, y: x + " " + y, words, "Start:")
print(sentence)  # Output: Start: hello world python

# Practical Application
# Finding the maximum value in a list:


nums = [3, 5, 2, 8, 1]
max_value = reduce(lambda x, y: x if x > y else y, nums)
print(max_value)  # Output: 8

#---------------------------------------------------------------------------------------------------------------------

# Real-World Applications

# Data Transformation
# Using map() for data preparation:

prices = ["$5.00", "$3.50", "$4.20"]
cleaned_prices = map(lambda x: float(x[1:]), prices)
print(list(cleaned_prices))  # Output: [5.0, 3.5, 4.2]

# Data Cleaning
# Using filter() to remove invalid data:

ages = [25, -1, 34, 0, 22]
valid_ages = filter(lambda x: x > 0, ages)
print(list(valid_ages))  # Output: [25, 34, 22]

# Aggregation
# Using reduce() for cumulative calculations:

sales = [100, 200, 300, 400]
total_sales = reduce(lambda x, y: x + y, sales)
print(total_sales)  # Output: 1000

#---------------------------------------------------------------------------------------------------------------------