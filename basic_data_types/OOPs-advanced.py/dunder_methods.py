'''

Dunder methods, also known as magic methods or special methods, are predefined methods in Python that allow 
developers to use custom objects with Python's built-in syntax and functionalities (like arithmetic operations, 
comparisons, string representations, and more). These methods are surrounded by double underscores 
(hence the name "dunder").

Dunder methods make classes more Pythonic by enabling object-oriented programming features and operator 
overloading.

'''

#------------------------------------- Dunder (Magic) Methods in Python ------------------------------------

# Dunder methods, also known as magic methods or special methods, are predefined methods in Python that 
# allow developers to use custom objects with Python's built-in syntax and functionalities 
# (like arithmetic operations, comparisons, string representations, and more).
# These methods are surrounded by double underscores (hence the name "dunder").

# Dunder methods make classes more Pythonic by enabling object-oriented programming features and operator 
# overloading.

#------------------------------------------------------------------------------------------------------------
# Core Concepts of Dunder Methods
#------------------------------------------------------------------------------------------------------------

# 1. Initialization and Representation

#------------------------------------------------------------------------------------------------------------
# __init__: Called when an object is initialized.
# __str__: Provides a readable string representation of an object.
# __repr__: Provides a detailed, developer-friendly string representation.

#------------------------------------------------------------------------------------------------------------

# 2. Arithmetic Operators

#------------------------------------------------------------------------------------------------------------
# __add__, __sub__, __mul__, etc., allow operator overloading for custom objects.
#------------------------------------------------------------------------------------------------------------

# 3. Comparison Operators

#------------------------------------------------------------------------------------------------------------
# __eq__, __lt__, __gt__, etc., enable custom comparison logic.
#------------------------------------------------------------------------------------------------------------

# 4. Container-Like Behavior

#------------------------------------------------------------------------------------------------------------
# __getitem__, __setitem__, __delitem__ allow objects to mimic container types like lists or dictionaries.
#------------------------------------------------------------------------------------------------------------

# 5. Object Lifecycle

#------------------------------------------------------------------------------------------------------------
# __new__: Controls object creation.
# __del__: Defines cleanup logic before an object is destroyed.
#------------------------------------------------------------------------------------------------------------


# 6. Other Advanced Functionalities
#------------------------------------------------------------------------------------------------------------
# __call__: Makes an instance callable like a function.
# __len__: Defines the behavior of len().
# __iter__: Enables iteration over an object.
#------------------------------------------------------------------------------------------------------------
