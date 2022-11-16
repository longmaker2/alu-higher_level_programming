#!/usr/bin/python3
'''a function that appends a string at the end of a text file'''


def append_write(filename="", text=""):
    '''function to write text to a file'''
    with open(filename, 'a+') as f:
        return f.write(text)
