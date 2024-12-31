#---------------------------------------------------------------------------------------------------------------------
# 1. map()
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