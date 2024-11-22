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

#----------------------------------------  Immutability --------------------------------------------

'''
Strings are immutable, meaning their content cannot be changed after creation.
'''
s = "Hello"
# s[0] = 'J'  # This will raise an error
s = s.replace("H", "J")  # Creates a new string
print(s)  # "Jello"

'''
In-Depth Explanation of Immutability
Memory Management
Immutability ensures memory efficiency and thread safety.
If strings were mutable, modifying one string could unintentionally affect other variables referencing the same string.
Example:

'''
s1 = "Hello"
s2 = s1  # Both `s1` and `s2` point to the same memory
s1 = s1.replace("H", "J")  # `s1` now points to a new string
print(s1)  # "Jello"
print(s2)  # "Hello"


# ------------------------------------------------ Basic Methods ----------------------------------------
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


#-------------------------------------------------------------------------------------------------------
#a. Case Modification

s = "Hello World"

print("Lowercase:", s.lower())  # Output: Lowercase: hello world
print("Uppercase:", s.upper())  # Output: Uppercase: HELLO WORLD
print("Title Case:", s.title())  # Output: Title Case: Hello World
print("Swap Case:", s.swapcase())  # Output: Swap Case: hELLO wORLD
print("Capitalize:", s.capitalize())  # Output: Capitalize: Hello world

#-------------------------------------------------------------------------------------------------------
# b. Alignment

s = "Hello"

print("Centered:", s.center(20, '-'))  # Output: Centered: -------Hello--------
print("Left Justified:", s.ljust(20, '*'))  # Output: Left Justified: Hello**************
print("Right Justified:", s.rjust(20, '*'))

#-------------------------------------------------------------------------------------------------------
# c. Splitting and Joining

s = "apple,banana,cherry"

# Splitting
split_list = s.split(',')
print("Split List:", split_list)  # Output: Split List: ['apple', 'banana', 'cherry']

# Joining
joined_string = '-'.join(split_list)
print("Joined String:", joined_string)  # Output: Joined String: apple-banana-cherry

#-------------------------------------------------------------------------------------------------------
# d. Trimming

s = "   Hello World   "

print("Stripped:", s.strip())  # Output: Stripped: Hello World
print("Left Stripped:", s.lstrip())  # Output: Left Stripped: Hello World   
print("Right Stripped:", s.rstrip())  # Output: Right Stripped:    Hello World
#-------------------------------------------------------------------------------------------------------

# e. String Queries

s = "Hello World"

print("Starts with 'Hello':", s.startswith("Hello"))  # Output: True
print("Ends with 'World':", s.endswith("World"))  # Output: True
print("Contains 'World':", "World" in s)  # Output: True
print("Is Alphabetic:", s.isalpha())  # Output: False
print("Is Alphanumeric:", "Hello123".isalnum())  # Output: True
print("Is Digit:", "12345".isdigit())  # Output: True
print("Is Lowercase:", s.islower())  # Output: False
print("Is Uppercase:", s.isupper())  # Output: False
print("Is Space:", "   ".isspace())  # Output: True

#-------------------------------------------------------------------------------------------------------
# 5. Advanced String Operations
# a. Replace

s = "apples are red"
modified = s.replace("apples", "oranges")
print("Modified:", modified)  # Output: Modified: oranges are red

#-------------------------------------------------------------------------------------------------------
# b. Find and Index

s = "find the needle in the haystack"
print("First occurrence of 'needle':", s.find("needle"))  # Output: 10
print("First occurrence of 'haystack':", s.index("haystack"))  # Output: 21

#-------------------------------------------------------------------------------------------------------
# c. Count

s = "banana"
print("Count of 'a':", s.count('a'))  # Output: 3

#-------------------------------------------------------------------------------------------------------
# d. Partition

s = "apple-banana-cherry"
print("Partition on '-':", s.partition('-'))  
# Output: Partition on '-': ('apple', '-', 'banana-cherry')

#-------------------------------------------------------------------------------------------------------
# e. Translate

s = "apple"
translation_table = str.maketrans("aep", "xyz")
translated = s.translate(translation_table)
print("Translated:", translated)  # Output: xzzly
#-------------------------------------------------------------------------------------------------------