#!/usr/bin/env python3
""" Task 1 """
import typing
import uuid
import redis


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Callable):
        """ gets value and converts it to the desired format"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        elif value is not None:
            return value

    def get_str(self, key: str) -> str:
        """get string"""
        return self.get(key, str)

    def get_int(self, key: str) -> str:
        """get int"""
        return self.get(key, int)
