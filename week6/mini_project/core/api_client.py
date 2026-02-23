"""A resilient API client that retries on failure."""
import time
import urllib.request
import urllib.error

from .exceptions import APIError, APITimeoutError, APIResponseError
from .logger_config import setup_logger

logger = setup_logger("API_Client")

class ResilientAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, retries=3):
        url = self.base_url + endpoint
        
        for attempt in range(1, retries + 1):
            try:
                logger.info(f"Attempt {attempt}: Calling {url}")
                
                # Basic urllib call
                req = urllib.request.Request(url, headers={'User-Agent': 'TestClient'})
                response = urllib.request.urlopen(req, timeout=3)
                
                logger.info("Call successful!")
                return response.read().decode('utf-8')
                
            except urllib.error.HTTPError as e:
                logger.error(f"HTTP Error {e.code}: {e.reason}")
                if attempt == retries:
                    raise APIResponseError("Max retries reached on HTTP error.", e.code)
                    
            except (urllib.error.URLError, TimeoutError) as e:
                logger.error(f"Timeout/Network Error: {e}")
                if attempt == retries:
                    raise APITimeoutError("Request timed out or network failed.")
                    
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                raise APIError("Something went very wrong.")
            
            # Exponential backoff sleep before trying again
            sleep_time = 2 ** attempt
            logger.warning(f"Waiting {sleep_time} seconds before trying again...")
            time.sleep(sleep_time)
