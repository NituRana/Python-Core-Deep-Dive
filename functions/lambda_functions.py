#------------------------------------------------------------------------------------------------------------
#                               In-Depth Guide to Lambda Functions in Python 
#------------------------------------------------------------------------------------------------------------

'''
A lambda function is an anonymous function in Python, defined using the lambda keyword. It can have any number of arguments but only one expression. The expression is evaluated, and the result is returned.

Syntax

lambda arguments: expression


lambda: Indicates the creation of a lambda function.
arguments: Inputs to the function (like parameters in regular functions).
expression: A single operation or computation that is evaluated and returned.

'''
add = lambda x, y: x + y
print(add(3, 5))

#------------------------------------------------------------------------------------------------------------
# Basic Usage
# a. Single Argument

square = lambda x: x ** 2
print(square(4))  # Output: 16

#------------------------------------------------------
# b. Multiple Arguments

multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

#------------------------------------------------------
# c. No Arguments

greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

#------------------------------------------------------------------------------------------------------------
# 3. Advanced Usage


# a. Using Lambda with Built-In Functions
#----------------------- 1. -------------------------------

# map()
# Applies a function to each item in an iterable.

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]

#--------------------------- 2. ---------------------------
# filter()
# Filters items based on a condition.


nums = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]

#------------------------------ 3. ------------------------
# reduce()
# Applies a rolling computation to a sequence (from functools).


from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 120

#------------------------------------------------------------------------------------------------------------
# Sorting with Lambda
# Sorting by Key

data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

#------------------------------ 1. ------------------------

words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']

#------------------------------------------------------------------------------------------------------------
# 7. Summary
# Lambda functions offer a concise and efficient way to write small, single-expression functions. They are particularly useful for:

'''
1. Functional programming (map, filter, reduce).
2. Custom sorting.
3. Event handling in GUIs.
4. Inline operations that are short-lived.
5. Final Example: Complex Lambda in Action
'''

employees = [
    {'name': 'Alice', 'salary': 70000},
    {'name': 'Bob', 'salary': 80000},
    {'name': 'Charlie', 'salary': 60000}
]

# Filter employees with salary > 65000 and sort by salary
filtered_sorted = sorted(
    filter(lambda e: e['salary'] > 65000, employees),
    key=lambda e: e['salary']
)

print(filtered_sorted)
# Output:
# [{'name': 'Alice', 'salary': 70000}, {'name': 'Bob', 'salary': 80000}]