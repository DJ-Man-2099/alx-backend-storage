#!/usr/bin/env python3
""" Task 1 """
from typing import Callable, Optional, Union
import uuid
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Creates and returns function that increments the count \
        for that key every time the method is called and returns \
        the value returned by the original method"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Increments count """
        name = method.__qualname__
        # Don't assign self to another variable
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """ gets value and converts it to the desired format"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        elif value is not None:
            return value

    def get_str(self, key: str) -> str:
        """get string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """get int"""
        return self.get(key, int)
