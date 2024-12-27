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