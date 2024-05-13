#!/usr/bin/env python3
""" 11th Task """
from typing import Dict, List
from pymongo.collection import Collection


def update_topics(mongo_collection, name,
                  topics):
    """ List all documents in Python """
    mongo_collection.update_one({"name": name},
                                {"$set": {"topics": topics}})
