#!/usr/bin/env python3
""" 11th Task """
from typing import Dict, List
from pymongo.collection import Collection
from bson import ObjectId


def update_topics(mongo_collection: Collection, name: str,
                  topics: List[str]):
    """ List all documents in Python """
    mongo_collection.update_one({"name": name},
                                {"$set": {"topics": topics}})
