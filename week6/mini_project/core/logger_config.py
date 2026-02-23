"""Logging configuration mapped to week 6 practice."""
import logging

def setup_logger(name):
    """Sets up a basic logger that outputs to console and a file."""
    # We use basicConfig just like the practice files!
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("api_caller.log")
        ]
    )
    return logging.getLogger(name)
