#!/usr/bin/env python3
""" Optional Task 1 """

import requests
from redis import Redis
from functools import wraps
from typing import Callable


def track_access(method: Callable) -> Callable:
    """Tracks Access"""
    @wraps(method)
    def wrapper(url, *args, **kwargs):
        """Wrapper"""
        redis_instance = Redis()
        key = f"count:{url}"
        cache = f"{url}"
        redis_instance.set(f"cached:{url}", 0)
        redis_instance.incr(key)
        # count = redis_instance.get(key)
        redis_instance.setex(cache, 10, redis_instance.get(cache))
        return method(url, *args, **kwargs)
    return wrapper


@track_access
def get_page(url: str) -> str:
    """uses the requests module
    to obtain the HTML content of a particular URL
    and returns it"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
