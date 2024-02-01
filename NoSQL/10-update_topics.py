#!/usr/bin/env python3

"""Function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )


if __name__ == '__main__':
    update_topics(mongo_collection, name, topics)
