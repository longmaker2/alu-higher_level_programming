#!/usr/bin/python3
"""displays the body of the response"""


import requests
import sys


if __name__ == "__main__":
    """sends the variable email"""
    url = sys.argv[1]
    reply = requests.get(url)
    if reply.status_code <= 400:
        print("{}".format(reply.text))
    else:
        print("Error code: {}".format(reply.status_code))
