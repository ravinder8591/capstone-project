import time
from app.logger import get_logger

monitor_logger = get_logger("monitoring")

def monitor(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        elapsed = time.time() - start
        monitor_logger.info(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper