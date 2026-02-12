"""
Week 6: Error Handling & Logging
Topic: Logging Basics

The logging module is essential for tracking what happens in your test scripts.
"""

import logging

# Exercise 1: Basic Configuration
# TODO: Use logging.basicConfig to set the level to DEBUG.
# TODO: 2. Log a message at each level: debug, info, warning, error, critical.

# Your code here:
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Exercise 2: Logging to a File
# TODO: Configure logging to write to a file named 'app.log'.
# TODO: 2. Log a few messages and check the file content.

# Your code here:
# Note: Re-configuring basicConfig doesn't work once set. 
# Usually, you'd do this at the start.
# For practice, we'll just demonstrate the concepts.
logging.basicConfig(filename='app.log', level=logging.INFO, force=True)
logging.info("Logging to file now...")

# Exercise 3: Logging Variables
# TODO: Log an error message that includes a variable value (e.g., "Failed to process item: {item}").

# Your code here:
item = "process_123"
logging.error(f"Failed to process item: {item}")
