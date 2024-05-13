#!/usr/bin/env python3
""" 9th Task """
from typing import Dict, List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[Dict]:
    """ List all documents in Python """
    return mongo_collection.find()
