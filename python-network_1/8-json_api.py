#!/usr/bin/python3
"""takes in a letter and sends a POST"""
import requests
import sys

if __name__ == '__main__':
    try:
        lett = sys.argv[1]
    except IndexError:
        lett = ""
    reply = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": lett}
    )
    try:
        json_response = reply.json()
        if reply.headers.get("Content-Type") == 'application/json':
            if len(json_response) > 0:
                print("[{}] {}".format(
                    json_response["id"],
                    json_response["name"])
                )
            else:
                print("No result")
    except:
        print("Not a valid JSON")
