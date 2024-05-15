#!/usr/bin/env python3
""" Task 1 """
import typing
import uuid
import redis
import functools


def count_calls(method: typing.Callable) -> typing.Callable:
    """takes a single method Callable argument
    and returns a Callable"""
    @functools.wraps(method)
    def wrapper(*args: typing.List, **kwds: typing.Dict) -> typing.Callable:
        name = method.__qualname__
        """ Increments count """
        redis_instance = args[0]
        redis_instance._redis.incr(name)
        return method(*args, **kwds)
    return wrapper


class Cache:
    """Cache class"""

    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Optional[typing.Callable] = None) \
            -> typing.Union[str, bytes, int, float]:
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
