# 2. Strings
'''
Strings in Python are sequences of Unicode characters and immutable. They’re a fundamental type, extensively used in all programming domains.
'''

#a) Memory Management
'''
When a string is modified, Python creates a new string instead of changing the original.
Uses interning for optimization:
Strings with simple, alphanumeric content may share memory.
'''

a = "hello"
b = "hello"
print(a is b)  # True (both point to the same memory)


#b) String Manipulations
'''
Python provides powerful methods for strings:
Splitting and Joining
'''

text = "Python is awesome"
words = text.split()  # ['Python', 'is', 'awesome']
print("Joined:", "-".join(words))  # Python-is-awesome

#-------------------------Advanced String Formatting --------------------------------------------
#-----------------------1. f-strings (Python 3.6+) ----------------------------------------------

name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Alice is 30 years old.

#----------------------------------------------------------------------------------------------
#-----------------------1. Template Strings (Safe Substitution):-------------------------------
from string import Template
t = Template("$name is $age years old.")
print(t.substitute(name="Bob", age=25))  # Bob is 25 years old.

#------------------------------Efficient String Concatenation:---------------------------------

'''
Using ''.join() is faster than + for large concatenations:
'''

strings = ["a"] * 10
result = ''.join(strings)

# a) Immutability

'''
Strings are immutable, meaning their content cannot be changed after creation.
'''
s = "Hello"
# s[0] = 'J'  # This will raise an error
s = s.replace("H", "J")  # Creates a new string
print(s)  # "Jello"


# ----------------------------------------- Basic Methods ----------------------------------------
'''
Strings offer numerous methods for manipulation:
'''
text = "Python Programming"
print("Length:", len(text))  # 18
print("Lowercase:", text.lower())  # "python programming"
print("Uppercase:", text.upper())  # "PYTHON PROGRAMMING"
print("Find 'Prog':", text.find("Prog"))  # 7
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))  # "Java Programming"
print("Split by space:", text.split())  # ['Python', 'Programming']