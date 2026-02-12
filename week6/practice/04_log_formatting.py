"""
Week 6: Error Handling & Logging
Topic: Log Formatting

Clean logs help you debug faster.
"""

import logging

# Exercise 1: Custom Format
# TODO: Create a formatter that includes: timestamp, level name, and message.
# TODO: 2. Apply this formatter to a stream handler and add it to the logger.

# Your code here:
logger = logging.getLogger("test_logger")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Debug message with formatting!")

# Exercise 2: Log Levels in Practice
# TODO: Create a function that logs 'INFO' when it starts and 'ERROR' if it fails.
# TODO: 2. Call it with an input that causes it to fail.

# Your code here:
def risky_operation(value):
    logger.info(f"Starting operation with value: {value}")
    try:
        result = 10 / value
        logger.info("Operation successful.")
        return result
    except ZeroDivisionError:
        logger.error("Operation failed: Division by zero!")

risky_operation(0)

# Exercise 3: Advanced Formatting
# TODO: Add the filename and line number to the log format.
#          Hint: Use %(filename)s and %(lineno)d in the format string.

# Your code here:
adv_formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
handler.setFormatter(adv_formatter)
logger.info("Advanced formatting activated!")
