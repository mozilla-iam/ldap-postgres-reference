#!/usr/bin/python
import pprint

"""
Prints all messages from the queue to screen.
"""
from lib import stream

if __name__ == "__main__":
    p = stream.Subscribe()
    for record in p.messages():
        print(record)
