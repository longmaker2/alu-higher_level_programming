#!/usr/bin/python3
'''a function that creates an Object from a “JSON file”:'''


import json


def load_from_json_file(filename):
    '''Function that does the work'''
    with open(filename, 'r') as f:
        return json.load(f)
