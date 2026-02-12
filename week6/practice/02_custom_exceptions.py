"""
Week 6: Error Handling & Logging
Topic: Custom Exceptions

In AI testing, we often need specific exceptions for API failures or validation errors.
"""

# Exercise 1: Defining a Custom Exception
# TODO: 1. Define a class 'ValidationError' that inherits from Exception.

# Your code here:
class ValidationError(Exception):
    pass

# Exercise 2: Raising Exceptions
# TODO: Create a function 'validate_age(age)' that raises ValidationError if age is negative.
# TODO: 2. Call the function with a negative number and catch the custom exception.

# Your code here:
def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative.")
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Caught custom exception: {e}")

# Exercise 3: Exception with Custom Data
# TODO: Update ValidationError to accept an error_code in __init__.
# TODO: 3. Raise it and print both the message and the error_code in the except block.

# Your code here:
class DetailedValidationError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

try:
    raise DetailedValidationError("Invalid input data", 400)
except DetailedValidationError as e:
    print(f"Error: {e}, Code: {e.error_code}")
