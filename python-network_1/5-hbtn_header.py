#!/usr/bin/python3
"""sends a request to the URL and displays the value of the variable"""


import requests
import sys


if __name__ == "__main__":
    """shows value of variable"""
    url = sys.argv[1]
    reply = requests.get(url)
    print("{}".format(reply.headers.get('X-Request-Id')))
