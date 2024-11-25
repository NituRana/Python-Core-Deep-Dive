#=======================================================================================================
#-------------------------------------------- Lists in Python ------------------------------------------
#=======================================================================================================

'''
What is a List?
Definition: A list is an ordered, mutable, and iterable collection that can hold items of any data type.


Key Properties:

Ordered: Items have a fixed order, and you can access them by their index.
Mutable: Elements can be added, removed, or changed.
Dynamic: Can grow or shrink in size.
Heterogeneous: Can store elements of different data types (e.g., ["Hello", 42, 3.14, True]).

'''
# --------------------------------------------- Key Operations ------------------------------------------
#---------------------------------------------------------------------------------------------------------
# 1. Creating a List
# Lists can be created using square brackets [] or the list() constructor.


# Empty list
empty_list = []
empty_list_constructor = list()

numbers = [1, 2, 3, 4]# Homogeneous list
mixed = ["apple", 3.14, True, [1, 2, 3]] # Heterogeneous list

print(empty_list, numbers, mixed)
# Output: [] [1, 2, 3, 4] ['apple', 3.14, True, [1, 2, 3]]


#---------------------------------------------------------------------------------------------------------
# 2. Accessing Elements
# Lists support indexing and slicing.

fruits = ["apple", "banana", "cherry"]

# 2.1: Access by index
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry

# 3.1: Slicing
print(fruits[1:])  # Output: ['banana', 'cherry']

#---------------------------------------------------------------------------------------------------------
# 3. Modifying a List
# Lists are mutable, so elements can be added, removed, or replaced.

numbers = [1, 2, 3]

# Replace
numbers[1] = 42
print(numbers)  # Output: [1, 42, 3]

# Add
numbers.append(99)
print(numbers)  # Output: [1, 42, 3, 99]

# Remove
numbers.remove(42)
print(numbers)  # Output: [1, 3, 99]
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


#----------------------------------------------- Advanced Features ---------------------------------------
# 1. List Comprehensions
# A concise way to create new lists by applying an operation to each element of an iterable.

# Example: Generating squares of numbers

numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16]

#---------------------------------------------------------------------------------------------------------
# With conditions:

# Even squares only
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # Output: [4, 16]

#---------------------------------------------------------------------------------------------------------
# 2. Common Methods
# Method	Description	Example
# append()	Adds an element to the end of the list	
numbers.append(10)
# extend()	Adds all elements from another iterable	
numbers.extend([11, 12])
# insert()	Inserts an element at a specific index	
numbers.insert(1, 42)
# remove()	Removes the first occurrence of a value	
numbers.remove(42)
# pop()	Removes and returns an element by index	
numbers.pop(2)
# index()	Returns the index of the first occurrence of a value	
numbers.index(10)
# sort()	Sorts the list in ascending order	
numbers.sort()
# reverse()	Reverses the list in place
numbers.reverse()

#==========================================================================================================
#-------------------------------------------- Applications of Lists ---------------------------------------
#==========================================================================================================

# 1. Storing Dynamic Data
# Lists are ideal for managing data that changes over time, such as a shopping cart.

cart = []
cart.append("apple")
cart.append("banana")
cart.remove("apple")
print(cart)  # Output: ['banana']

#---------------------------------------------------------------------------------------------------------
# 2. Iterative Processing
# Lists are iterable, making them perfect for loops.


numbers = [1, 2, 3]
for num in numbers:
    print(num)

#---------------------------------------------------------------------------------------------------------
# 3. Matrix Representation
# Nested lists can represent matrices.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[1][2])  # Output: 6

#==========================================================================================================
#-------------------------------------------- Pitfalls and Gotchas ---------------------------------------
#==========================================================================================================

# 1. Reference vs. Copy
# Mutating a list affects all references to it.

original = [1, 2, 3]
copy = original
copy[0] = 42
print(original)  # Output: [42, 2, 3] (changes reflect in both)

# Solution: Use slicing or copy() for a shallow copy.


copy = original[:]
# or
copy = original.copy()

#---------------------------------------------------------------------------------------------------------
# 2. Iterating While Modifying
# Directly modifying a list while iterating can cause unexpected behavior.

numbers = [1, 2, 3]
for num in numbers:
    if num == 2:
        numbers.remove(num)
print(numbers)  # Output: [1, 3] (skips elements)

# Solution: Use list comprehension or iterate over a copy.

numbers = [num for num in numbers if num != 2]
