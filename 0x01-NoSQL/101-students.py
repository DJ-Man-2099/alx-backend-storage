#!/usr/bin/env python3
""" 2nd Optional Task """
from typing import Dict, List
from pymongo.collection import Collection


def top_students(mongo_collection):
    """ List all documents in Python """
    return mongo_collection.aggregate([{
        "$set": {
            "averageScore": {"$avg": "$topics.score"}
        },
    }, {
        "$sort": {
            "averageScore": -1
        }
    }])
