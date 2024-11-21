#1. Numbers
'''

(a) Integers
Integers are whole numbers without a decimal point.
Example: 10, -20, 0

'''
# 1. 1 Integer operations
a = 10
b = 5
print("Addition:", a + b)   # 15
print("Subtraction:", a - b)  # 5
print("Multiplication:", a * b)  # 50
print("Division (float):", a / b)  # 2.0
print("Division (integer):", a // b)  # 2
print("Modulus:", a % b)  # 0
print("Power:", a ** b)  # 100000


'''

(b) Floats
Floating-point numbers are numbers with a decimal point.
Example: 3.14, -0.001

'''

# 1. 2 Float operations
'''
Represent real numbers.
Stored as IEEE 754 double precision (64-bit).
Includes a mantissa and an exponent.
Advanced Insights
Precision Issues: Floating-point numbers can have rounding errors.
'''

x = 0.1 + 0.2
print(x)  # 0.30000000000000004
# Use decimal module for precise calculations.

from decimal import Decimal
x = Decimal('0.1') + Decimal('0.2')
print(x)  # 0.3

x = 5.5
y = 2.2
print("Addition:", x + y)  # 7.7
print("Subtraction:", x - y)  # 3.3
print("Multiplication:", x * y)  # 12.1
print("Division:", x / y)  # 2.5



# 1. 2 Complex numbers

'''
#Complex Numbers
Complex numbers have a real part and an imaginary part (denoted by j).
Example: 3 + 4j
'''

z1 = 3 + 4j
z2 = 1 - 2j
print("Addition:", z1 + z2)  # (4+2j)
print("Subtraction:", z1 - z2)  # (2+6j)
print("Multiplication:", z1 * z2)  # (11-2j)
print("Division:", z1 / z2)  # (-1+2j)
print("Absolute value:", abs(z1))  # 5.0


# 1. 4 Bitwise Operations: Efficient for low-level programming.


a = 5  # Binary: 101
b = 3  # Binary: 011
print("Bitwise AND:", a & b)  # 1 (Binary: 001)
print("Bitwise OR:", a | b)   # 7 (Binary: 111)
print("Bitwise XOR:", a ^ b)  # 6 (Binary: 110)
print("Bitwise Shift Left:", a << 1)  # 10 (Binary: 1010)
print("Bitwise Shift Right:", a >> 1)  # 2 (Binary: 10)


