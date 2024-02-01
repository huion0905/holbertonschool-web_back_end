#!/usr/bin/env python3

"""Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    all_documents = mongo_collection.find({})
    if all_documents:
        return all_documents
    else:
        return []


if __name__ == '__main__':
    list_all(mongo_collection)
