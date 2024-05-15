#!/usr/bin/env python3
""" Optional Task 1 """

import requests
import redis
from functools import wraps
from typing import Any, Callable, Dict, List


def track_access(method: Callable) -> Callable:
    """Tracks Access"""
    @wraps(method)
    def wrapper(url, *args, **kwargs):
        """Wrapper"""
        redis = redis.Redis()
        key = f"count:{url}"
        cache = f"{url}"
        redis.incr(key)
        # count = redis_instance.get(key)
        cached = redis.get(cache)
        if cached:
            return cached.decode('utf-8')
        response = method(url, *args, **kwargs)
        redis.setex(cache, 10, response)
        return response
    return wrapper


@track_access
def get_page(url: str) -> str:
    """uses the requests module
    to obtain the HTML content of a particular URL
    and returns it"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    """Main function"""
    get_page("http://slowwly.robertomurray.co.uk")
