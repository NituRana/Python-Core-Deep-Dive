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