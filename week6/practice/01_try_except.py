"""
Week 6: Error Handling & Logging
Topic: Try/Except Blocks

This practice file introduces basic error handling in Python.
"""

# Exercise 1: Basic Try/Except
# TODO: Create a variable 'number' and try to divide 10 by 'number'.
# TODO: Wrap this in a try/except block to catch ZeroDivisionError.
# TODO: 3. Print a friendly message if division by zero occurs.

# Your code here:
try:
    number = 0
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Exercise 2: Catching Multiple Exceptions
# TODO: Create a list 'data' with some values.
# TODO: Try to access an index that doesn't exist AND try to divide by zero.
# TODO: 3. Catch both IndexError and ZeroDivisionError separately.

# Your code here:
try:
    data = [1, 2, 3]
    # value = data[5]  # IndexError
    result = 10 / 0    # ZeroDivisionError
except IndexError:
    print("Index out of range!")
except ZeroDivisionError:
    print("Zero division error in multiple catch!")

# Exercise 3: The 'else' and 'finally' blocks
# TODO: Use a try block to open a file (that exists or not).
# TODO: Use 'else' to print a message if no error occurred.
# TODO: 3. Use 'finally' to print "Execution completed" regardless of errors.

# Your code here:
try:
    file = open("non_existent.txt", "r")
except FileNotFoundError:
    print("File not found error caught.")
else:
    print("File opened successfully.")
finally:
    print("Execution completed")
