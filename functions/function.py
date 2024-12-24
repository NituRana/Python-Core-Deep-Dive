#==========================================================================================================
#------------------------------------------------ Function ------------------------------------------------
#==========================================================================================================
'''
1. What is a Function?
A function is a reusable block of code that performs a specific task. It can take inputs (arguments), process them, and return a result.

Syntax of Function
'''
def function_name(parameters):
    """Optional docstring"""
    result = 2 * parameters
    # Body of the function
    return result

#-------------------------------------------- Advanced Function Concepts ------------------------------------
# a. Variable-Length Arguments
# Handle functions with arbitrary numbers of arguments.

# 1. Positional Arguments (*args):

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))

#-----------------------------------------------------------------------------------------------------------

# Keyword Arguments (**kwargs):

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC

#-----------------------------------------------------------------------------------------------------------
# b. First-Class Functions
# Functions in Python are first-class citizens, meaning:

'''
They can be assigned to variables.
They can be passed as arguments.
They can be returned from other functions.
'''

# 1. Assigning Functions to Variables:

def square(x):
    return x ** 2

sq = square
print(sq(5))  # Output: 25


# 2. Passing Functions as Arguments:
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply(double, 5))  # Output: 10

# 3. Returning Functions:
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10