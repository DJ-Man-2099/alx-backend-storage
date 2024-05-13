#!/usr/bin/env python3
""" 12th Task """
from typing import Dict, List
from pymongo.collection import Collection


def schools_by_topic(mongo_collection,
                     topic):
    """ List all documents in Python """
    schools = mongo_collection.find({"topics": topic})

    return list(schools)
