"""Custom exceptions for the API client."""

class APIError(Exception):
    """Base exception for all API errors."""
    pass

class APITimeoutError(APIError):
    """Raised when a request times out."""
    pass

class APIResponseError(APIError):
    """Raised when we get a bad status code like 404 or 500."""
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code
