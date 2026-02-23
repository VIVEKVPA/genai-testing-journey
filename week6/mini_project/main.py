"""Main script to demonstrate our resilient API caller."""
from core.api_client import ResilientAPIClient
from core.exceptions import APIError
from core.logger_config import setup_logger

logger = setup_logger("Main")

def main():
    logger.info("--- Starting Robust API Caller ---")
    client = ResilientAPIClient(base_url="https://httpbin.org")
    
    # Scenario 1: Successful Call
    try:
        logger.info("Testing a successful endpoint...")
        client.get("/get")
        logger.info("Success scenario passed!")
    except Exception as e:
        logger.error(f"Unexpected failure: {e}")
        
    print("\n" + "="*40 + "\n")
    
    # Scenario 2: Failing Call with Retries
    try:
        logger.info("Testing a failing endpoint (500 Server Error)...")
        client.get("/status/500", retries=2)
    except APIError as e:
        logger.error(f"Caught custom exception properly: {e}")

    logger.info("--- Demonstration Complete ---")

if __name__ == "__main__":
    main()
