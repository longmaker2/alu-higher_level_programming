#!/usr/bin/python3
'''a function that reads a text file and
prints it out'''


def read_file(filename=""):
    '''Reads the data from outside file '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
