
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


# Practical Applications of Generators
# 1. Generating Infinite Sequences

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(5):
    print(next(gen))
# Output:
# 0
# 1
# 2
# 3
# 4



# 2. Reading Large Files
# Generators are ideal for processing large files line-by-line without loading the entire file into memory.

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)


# Advanced Topics
# 1. Generator with send()
# The send() method can be used to send a value to the generator, resuming its execution and optionally changing its state.


def generator_with_send():
    value = yield "Start"
    while value < 5:
        value = yield value * 2

gen = generator_with_send()
print(next(gen))  # Output: Start
print(gen.send(2))  # Output: 4
print(gen.send(4))  # Output: 8


# 2. Generator throw()
# The throw() method raises an exception inside the generator.


def generator_with_throw():
    try:
        yield "Start"
        yield "Middle"
    except Exception as e:
        yield f"Exception caught: {e}"

gen = generator_with_throw()
print(next(gen))  # Output: Start
print(gen.throw(Exception("Error occurred")))
# Output: Exception caught: Error occurred



# 3. Generator close()
# The close() method stops the generator.


def closeable_generator():
    yield 1
    yield 2

gen = closeable_generator()
print(next(gen))  # Output: 1
gen.close()
# Any further calls to `next(gen)` will raise a StopIteration exception.