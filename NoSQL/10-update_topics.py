#!/usr/bin/env python3
"""10-update_topics"""


def update_topics(mongo_collection, name, topics):
    """Update all matching school documents with the given topics."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
