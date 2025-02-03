'''
1. Iterators
What is an Iterator?
An iterator is an object that allows sequential access to the elements of a collection (e.g., list, tuple, dictionary).
Implements two methods:
__iter__(): Returns the iterator object itself.
__next__(): Returns the next value in the sequence. Raises StopIteration when no items are left.
How to Create an Iterator
An iterator can be created from an iterable using the iter() function.

'''

# Example: Basic Iterator
nums = [1, 2, 3, 4]
iterator = iter(nums)  # Create an iterator

# Access elements using the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2

# Custom Iterator Class
'''
You can create your custom iterator by implementing the __iter__ and __next__ methods.

'''

# Custom Iterator Class
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):  # Makes the class an iterator
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # End of iteration
        value = self.current
        self.current += 1
        return value

# Usage
counter = Counter(1, 5)
for num in counter:
    print(num)  # Output: 1 2 3 4 5



'''
2. Generators
What is a Generator?
A generator is a simpler way to create iterators using functions and the yield keyword.
Instead of returning a value and terminating, the yield statement pauses the function, saving its state for the next call.
How to Create a Generator
Generators are created using functions or generator expressions.

Using a Function with yield
'''



# Example: Simple Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Usage
for num in count_up_to(5):
    print(num)  # Output: 1 2 3 4 5

# Using a Generator Expression
# Example: Generator Expression
squares = (x ** 2 for x in range(5))

# Usage
for square in squares:
    print(square)  # Output: 0 1 4 9 16

# Key Differences Between Iterators and Generators
# Feature	Iterator	Generator
# Creation	        Implement __iter__() and __next__() methods manually.	                    Use a function with yield.
# Syntax	        Requires more boilerplate code.	                                            Concise and easy to write.
# State             Maintenance	Must manually track state.	                                    Automatically maintains state between yields.
# Memory            Efficiency	Can be less memory efficient when dealing with large datasets.	Memory-efficient; produces items on demand.


# 4. Advantages of Generators
#----------------------------------------------------------------
# Lazy Evaluation: Values are generated on the fly, reducing memory usage.
# Ease of Use: Fewer lines of code compared to manual iterator implementation.
# Performance: Ideal for large datasets or streams where values are consumed sequentially.