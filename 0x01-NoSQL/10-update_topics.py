#!/usr/bin/env python3
'''a module to update a document'''


def update_topics(mongo_collection, name, topics):
    '''a function to update'''
    result = mongo_collection.update_many(
            {"name": name}, {"$set": {"topics": topics}}
            )
    return result
