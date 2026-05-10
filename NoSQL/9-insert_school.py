#!/usr/bin/env python3
"""9-insert_school"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new school document and return its id."""
    return mongo_collection.insert_one(kwargs).inserted_id
