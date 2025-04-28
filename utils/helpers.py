"""
Helper functions for logging and retry logic.
"""
import logging
import time
from functools import wraps

def setup_logging(log_level: str = 'INFO'):
    """
    Configure basic logging for the application.

    Args:
        log_level: Logging level (e.g., 'DEBUG', 'INFO').
    """
    # TODO: configure logging format and handlers
    logging.basicConfig(level=log_level)

def retry_on_exception(exceptions: tuple, max_retries: int = 3, backoff_factor: float = 0.3):
    """
    Decorator to retry a function call on specified exceptions.

    Args:
        exceptions: Tuple of exception classes to catch.
        max_retries: Maximum number of retry attempts.
        backoff_factor: Backoff time multiplier between retries.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: implement retry logic with exponential backoff
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < max_retries - 1:
                        sleep_time = backoff_factor * (2 ** attempt)
                        time.sleep(sleep_time)
                        continue
                    else:
                        raise
        return wrapper
    return decorator