# 2. Strings

# a) Immutability
'''
Strings are immutable, meaning their content cannot be changed after creation.
'''
s = "Hello"
# s[0] = 'J'  # This will raise an error
s = s.replace("H", "J")  # Creates a new string
print(s)  # "Jello"


# b) Basic Methods
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