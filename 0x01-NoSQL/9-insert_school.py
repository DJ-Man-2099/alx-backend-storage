#!/usr/bin/env python3
""" 10th Task """
from typing import Dict, List
from pymongo.collection import Collection
from bson import ObjectId


def insert_school(mongo_collection, **kwargs):
    """ Inserts new document in collection based on kwargs """
    id_obj = mongo_collection.insert_one(kwargs)

    return id_obj.inserted_id
