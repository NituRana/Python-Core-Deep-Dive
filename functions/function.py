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