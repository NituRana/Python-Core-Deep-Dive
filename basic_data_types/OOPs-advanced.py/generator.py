
'''
A generator in Python is a special type of iterator that simplifies the process of creating iterators. It allows you to 
iterate through a sequence of values without having to store them all in memory at once. Generators are particularly useful 
when working with large datasets or infinite sequences, as they yield values one at a time on demand.

'''

'''

Key Concepts of Generators
Generators vs Normal Functions
A generator is a function that uses the yield statement to return a value and pause its execution. The next time it's called, it resumes execution right after the yield statement.

yield Statement

Works like a return statement but pauses the function.
Each call to the generator function produces a generator object.
Memory Efficiency
Generators produce values on-the-fly, so they are more memory-efficient than creating and storing a complete list of values.

Generator Expressions
Similar to list comprehensions, but enclosed in parentheses (()), not brackets ([]), and produce a generator object.

State Persistence
Generators maintain their state between successive calls.

'''

# 1.  Basic Example: Generator Function

def simple_generator():
    yield 1  # First value
    yield 2  # Second value
    yield 3  # Third value

# Using the generator
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration


# How yield Works
# The yield statement pauses the generator and saves its state (including local variables). On the next call, it resumes from where it left off.

# State Persistence

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count  # Pause and return count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5