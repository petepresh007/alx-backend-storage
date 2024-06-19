#!/usr/bin/env python3
'''a module to insert using kwqrgs'''


def insert_school(mongo_collection, **kwargs):
    '''function to insert into a document'''
    ins = mongo_collection.insert_one(kwargs)
    return ins.inserted_id
