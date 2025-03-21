#==========================================================================================================
#------------------------------------------------ Sets in Python ------------------------------------------
#==========================================================================================================


'''
What is a Set?

A set in Python is a collection data type that is:

1. Unordered: Elements are not stored in any particular order.
2. Unique: Duplicate elements are automatically removed.
3. Mutable: You can add or remove items from a set.
4. Iterable: You can loop through set elements.

'''
#----------------------------------------------------- Key Properties ---------------------------------------------

# No Duplicates: Useful for eliminating duplicate data.
# Hashable Elements Only: Elements in a set must be immutable (e.g., strings, numbers, tuples).
# Unordered Nature: Unlike lists, the order of elements is not guaranteed.

#-------------------------------------------------------------------------------------------------------------------
#===================================================================================================================
#----------------------------------------------------- Key Operations ---------------------------------------------
# 1. Creating a Set
# Sets are created using curly braces {} or the set() constructor.

# Empty set
empty_set = set()  # Use set(), not {}
print(empty_set)  # Output: set()

# Set with values
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Using set() with a sequence
unique_chars = set("hello")
print(unique_chars)  # Output: {'h', 'e', 'l', 'o'}

#-------------------------------------------------------------------------------------------------------------------
# 2. Adding and Removing Elements
# Add: Adds a single element.
# Update: Adds multiple elements.
# Remove/Discard: Removes an element.

fruits = {"apple", "banana"}

# Add
fruits.add("cherry")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Update
fruits.update(["date", "elderberry"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# Remove
fruits.remove("apple")  # Raises KeyError if 'apple' is not found
print(fruits)  # Output: {'banana', 'cherry', 'date', 'elderberry'}

# Discard (no error if the element does not exist)
fruits.discard("fig")
print(fruits)  # Output: {'banana', 'cherry', 'date', 'elderberry'}

#-------------------------------------------------------------------------------------------------------------------
# 3. Set Operations
# Python sets support mathematical set operations like union, intersection, difference, and symmetric difference.


A = {1, 2, 3}
B = {3, 4, 5}

# Union (A ∪ B)
print(A | B)  # Output: {1, 2, 3, 4, 5}

# Intersection (A ∩ B)
print(A & B)  # Output: {3}

# Difference (A - B)
print(A - B)  # Output: {1, 2}

# Symmetric Difference (A Δ B)
print(A ^ B)  # Output: {1, 2, 4, 5}

#------------------------------------------------------------------------------------------------------------------
# 4. Membership Testing
# Efficiently checks for the presence of an element in the set.

fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # Output: True
print("date" in fruits)   # Output: False

#------------------------------------------------------------------------------------------------------------------
# 5. Iterating Over a Set
# You can loop through the elements of a set.


for fruit in {"apple", "banana", "cherry"}:
    print(fruit)
# Output: (order not guaranteed)
# apple
# banana
# cherry
#------------------------------------------------------------------------------------------------------------------
#===================================================================================================================
#----------------------------------------------------- When to Use Sets -------------------------------------------

# 1. Removing Duplicates
# Sets automatically eliminate duplicate values.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

#------------------------------------------------------------------------------------------------------------------
# 2. Fast Membership Testing
# Membership testing (in) in sets is highly efficient, unlike lists or tuples.

# Testing membership in a large dataset
large_set = set(range(1_000_000))
print(999_999 in large_set)  # Output: True

#------------------------------------------------------------------------------------------------------------------
# 3. Set Algebra
# Useful for tasks like filtering data, comparing datasets, and more.

#------------------------------------------------------------------------------------------------------------------
#===================================================================================================================
#------------------------------------------- Advanced Features of  Sets -------------------------------------------

# 1. Frozen Sets
# A frozenset is an immutable version of a set. You can use it when you need a set but cannot allow modification.


A = frozenset([1, 2, 3])
print(A)  # Output: frozenset({1, 2, 3})

# Immutable, so this raises an error
# A.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

#------------------------------------------------------------------------------------------------------------------
# 2. Nested Sets (Using Frozen Sets)
# Because regular sets are mutable and unhashable, you can use frozensets to create nested sets.

nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)  # Output: {frozenset({1, 2}), frozenset({3, 4})}
#------------------------------------------------------------------------------------------------------------------
#===================================================================================================================
#------------------------------------------- Common Set Methods ----------------------------------------------------

# Method	Description	Example :

# add(x)	            | Adds an element x to the set	                    | s.add(1)
# remove(x)	            | Removes x (raises an error if x not found)	    | s.remove(1)
# discard(x)	        | Removes x (no error if x not found)	            | s.discard(1)
# clear()	            | Removes all elements	                            | s.clear()
# union(other)	        | Returns a new set with elements from both sets	| s.union(t)
# intersection(other)	| Returns a new set with common elements	        | s.intersection(t)
# difference(other)	    | Returns a new set with elements not in other	    | s.difference(t)
#------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- Applications of Sets ------------------------------------------------

# 1. Comparing Datasets
# Use sets to find unique, common, or missing elements between datasets.

# Finding common students
math_students = {"Alice", "Bob", "Charlie"}
science_students = {"Bob", "Diana"}

common_students = math_students & science_students
print(common_students)  # Output: {'Bob'}

#---------------------------------------------------
# 2. Removing Duplicate Words
# Process text to remove duplicate words.

text = "apple banana apple cherry banana"
unique_words = set(text.split())
print(unique_words)  # Output: {'apple', 'banana', 'cherry'}

#---------------------------------------------------
# 3. Optimizing Search Queries
# Use sets to find matching keywords quickly.
#------------------------------------------------------------------------------------------------------------------