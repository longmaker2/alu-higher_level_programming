#!/usr/bin/python3
'''a Python script that displays the value of the X-Request-Id variable'''


import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as reply:
        header = reply.info()
        print(header['X-Request-Id'])
