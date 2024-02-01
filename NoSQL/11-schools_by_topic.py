#!/usr/bin/env python3

"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    schools_with_topic = mongo_collection.find({"topics": topic})
    return list(schools_with_topic)


if __name__ == '__main__':
    update_topics(mongo_collection, name, topics)
