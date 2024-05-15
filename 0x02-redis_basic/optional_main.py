#!/usr/bin/env python3
"""
Optional Main file
"""
from time import sleep
from redis import Redis

get_page = __import__('web').get_page

redis = Redis()


url = "http://google.com"
print(get_page(url))
print("----------------------")

print(get_page(url))
print("----------------------")
print(redis.get(f"count:{url}"))

print(get_page(url))
print("----------------------")

print(get_page(url))
print("----------------------")

print(redis.get(f"count:{url}"))

sleep(10)

print(redis.get(f"count:{url}"))