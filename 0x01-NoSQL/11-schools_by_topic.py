#!/usr/bin/env python3
''' a module to find a particular user '''


def schools_by_topic(mongo_collection, topic):
    '''function for finding a user'''
    res = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [docs for docs in mongo_collection.find(res)]
