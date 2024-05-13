#!/usr/bin/env python3
""" 11th Task """


import typing


def update_topics(mongo_collection, name: str,
                  topics: typing.List[str]):
    """ List all documents in Python """
    mongo_collection.update_one({"name": name},
                                {"$set": {"topics": topics}})
