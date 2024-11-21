
#--------------------------------------------- Boolean Data Type ----------------------------------------------------
'''
The Boolean data type in Python represents one of two values: True or False. It is derived from Boolean algebra and is a subclass of the integer type. Booleans are fundamental in programming as they are used in conditional statements, loops, and logical operations.

'''
# ----------------------------------------------1. Boolean Basics ---------------------------------------------------
'''
Definition 
A Boolean in Python has two possible values:
True (equivalent to 1)
False (equivalent to 0)
Examples:
'''
x = True
y = False

print(type(x))  # Output: <class 'bool'>
print(type(y))  # Output: <class 'bool'>

# -------------------------------------2. Booleans as Subclasses of Integers ------------------------------------------
'''
In Python, Booleans are a subclass of int. This means:

True is equivalent to 1.
False is equivalent to 0.
Example:
'''
print(isinstance(True, int))  # Output: True
print(True + True)            # Output: 2 (1 + 1)
print(False + 1)              # Output: 1 (0 + 1)

# You can perform arithmetic operations with Booleans, as they are treated as 0 and 1.

# --------------------------------------------- 3. Boolean Context ---------------------------------------------------------
'''
Booleans are often used in expressions or conditions where Python expects a truth value. Python evaluates various data types as either True or False.

'''
    #Truthy and Falsy Values

'''
Truthy: Values considered as True in a Boolean context.
Falsy: Values considered as False in a Boolean context.
'''
    #Falsy Values in Python:
'''
1. None
2. False
3. 0 (any numeric type, e.g., 0.0, 0j)
4. '' or "" (empty string)
5. [] (empty list)
6. {} (empty dictionary)
7. () (empty tuple)
8. set() (empty set)
All other values are considered Truthy.
'''