#!/usr/bin/env python3
'''a module to to find documents using pymongo'''


def list_all(mongo_collection):
    '''a function to find'''
    document = mongo_collection.find()
    document_list = list(document)
    return document_list
