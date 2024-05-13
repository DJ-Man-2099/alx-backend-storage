#!/usr/bin/env python3
""" 10th Task """
from typing import Dict, List
from pymongo.collection import Collection
from bson import ObjectId


def insert_school(mongo_collection, **kwargs):
    """ List all documents in Python """
    return mongo_collection.insert_one(kwargs).inserted_id
