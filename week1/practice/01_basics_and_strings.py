# Week 1: Python Basics & Strings
# Topics Covered:
# - Strings: formatting, methods (upper, lower, etc.)
# - Numbers: Arithmetic operations

print("--- Strings ---")

# Print Welcome Message
message = 'Hello World'
print(f"Message: {message}")

# Difference between single quote and double quote
# Use double quotes if the string contains a single quote, or escape it.
#escape single quote using \ (backslash)
message_single_quote = 'Sourav\'s World'
print(f"Single Quote Escaped: {message_single_quote}")

#use double quotes if the string contains double quotes
message_double_quote = "Sourav's World"
print(f"Double Quote: {message_double_quote}")

# Multi-line comment (Docstring used as a string)
message_multi_line = """Sourav's World
And i learn and grow here"""
print(f"Multi-line String:\n{message_multi_line}")

print("\n--- String Operations ---")
message = 'Hello World'
print(f"Original Message: {message}")
print(f"Length of message: {len(message)}")
print(f"First letter [0]: {message[0]}")
print(f"Last letter [10]: {message[10]}")
print(f"First 5 letters [0:5]: {message[0:5]}")
print(f"First 5 letters [:5]: {message[:5]}")
print(f"Last 5 letters [6:]: {message[6:]}")
print(f"Lower case: {message.lower()}")
print(f"Upper case: {message.upper()}")
print(f"Count of 'l': {message.count('l')}")  # count of l - 3
print(f"Index of 'World': {message.find('World')}")  # find the index of World
print(f"Replaced 'World' with 'Universe': {message.replace('World', 'Universe')}")

new_message = message.replace('World', 'Universe')
print(f"New Message variable: {new_message}")

print("\n--- Key Methods for AI Testing ---")
# 1. strip() - Cleaning whitespace from LLM responses
response = "   The answer is 42.   "
clean_response = response.strip()
print(f"Original: '{response}'")
print(f"Cleaned: '{clean_response}'")

# 2. startswith() / endswith() - Checking response patterns
error_msg = "Error: Invalid API Key"
if error_msg.startswith("Error"):
    print("Detected an error!")

filename = "data.json"
if filename.endswith(".json"):
    print("Found a JSON file")

# 3. 'in' operator - Checking for keywords
text = "The model hallucinated."
if "hallucinated" in text:
    print("Found keyword: hallucinated")

# 4. split() & join() - Formatting outputs
csv_line = "apple,banana,cherry"
fruits = csv_line.split(',')
print(f"Split list: {fruits}")

clean_csv = " | ".join(fruits)
print(f"Joined string: {clean_csv}")

print("\n--- String Formatting ---")
greeting = 'Hello'
name = 'Sourav'
message = greeting + ', ' + name + '. Welcome to Python'
print(f"Concatenation: {message}")

# placeholder using .format()
message = '{}, {}. Welcome to Python'.format(greeting, name)
print(f".format() method: {message}")

# f-string (Formatted String Literals) - Recommended for Python 3.6+
message = f'{greeting.lower()}, {name}. Welcome to Python'
print(f"f-string: {message}")

# print(help(str.lower))

print("\n--- Prompt Engineering with f-strings ---")
role = "AI Assistant"
language = "Python"
temperature = 0.7

# Multi-line f-string (Crucial for System Prompts)
system_prompt = f"""
You are an {role}.
Specialty: {language}
Temperature: {temperature}

Instructions:
1. Be concise.
2. Show code examples.
"""
print(f"System Prompt:\n{system_prompt}")


print("\n--- Numbers ---")
num = 3.14
print(f"Type of {num}: {type(num)}")

# Arithmetic Operations
print(f"3 + 2 = {3 + 2}")  # Addition
print(f"3 - 2 = {3 - 2}")  # Subtraction
print(f"3 * 2 = {3 * 2}")  # Multiplication
print(f"3 / 2 = {3 / 2}")  # Division (float)
print(f"3 // 2 = {3 // 2}")  # Floor Division (integer)
print(f"3 % 2 = {3 % 2}")  # Modulus (remainder)
print(f"3 ** 2 = {3 ** 2}")  # Exponent (power)

# Comparison Operations
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater than:     3 > 2
# Less than:        3 < 2
# Greater or equal: 3 >= 2
# Less or equal:    3 <= 2
