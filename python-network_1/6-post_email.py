#!/usr/bin/python3
"""a Python script that takes in a URL """


import requests
import sys


if __name__ == "__main__":
    """sends the variable email"""
    url = sys.argv[1]
    email = sys.argv[2]
    context = {
        "email": email
    }
    reply = requests.post(url, data=context)
    print("{}".format(reply.text))
