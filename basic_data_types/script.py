# Handling Integers
print("---------------------- Integer Operations ------------------------")
a = 10
b = 3
print(f"a: {a}, b: {b}")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)  # Returns float
print("Floor Division:", a // b)  # Integer division
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\n-------------------- Type conversion: Integer to Float ---------------------")
# Type conversion: Integer to Float
a_float = float(a)
print("Converted to float:", a_float)

# Handling Floats
print("\n-------------------------- Float Operations -------------------------------")
x = 5.75
y = 2.5
print(f"x: {x}, y: {y}")
print("Addition:", x + y)
print("Rounding:", round(x))
print("Type Conversion (float to int):", int(x))  # Truncates the decimal

# Handling Strings
print("\n-------------------------- String Operations ------------------------------")
s1 = "Hello"
s2 = "World"
print(f"s1: {s1}, s2: {s2}")
print("Concatenation:", s1 + " " + s2)
print("Repetition:", s1 * 3)
print("Substring:", s1[1:4])  # Substring from index 1 to 3
print("Case conversion (Upper):", s1.upper())
print(f"Character at index 1: {s1[1]}")
print(f"Slicing: {s1[1:4]}")
print(f"Split: {s1.split('e')}")

print("\n-------------------------- Type Conversion: String to Integer/Float ------------------------------")
# Type Conversion: String to Integer/Float
num_str = "123"
print("String to Integer:", int(num_str))
print("String to Float:", float(num_str))

print("\n------------------------------------------ Boolean Logic --------------------------------------")
# Boolean Logic
print("\nBoolean Logic:")
is_raining = True
is_sunny = False
print(f"is_raining: {is_raining}, is_sunny: {is_sunny}")
print(f"is_raining and is_sunny: {is_raining and is_sunny}")
print(f"is_raining or is_sunny: {is_raining or is_sunny}")
print(f"not is_raining: {not is_raining}")