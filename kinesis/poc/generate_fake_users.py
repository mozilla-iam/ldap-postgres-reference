#!/usr/bin/python


"""
This generates a bunch of fake users
and pushes them into the kinesis stream.
"""

from lib import fake
from lib import stream

# How many users would you like to generate?

NUMBER_OF_USERS = 1000

pub = stream.Publish()

if __name__ == "__main__":
    for _ in range(0, NUMBER_OF_USERS):
        print pub.put_message(
            str(
                fake.User().enriched_profile()
            )
        )

    print "{num} users have been pushed into the queue.".format(
        num=NUMBER_OF_USERS
    )
