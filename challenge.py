#!/usr/bin/env python
from nylas import APIClient
import json

config = json.load(open('config.json'))

def main():
    client = APIClient(config['NYLAS_APP_ID'], config['NYLAS_APP_SECRET'], config['NYLAS_ACCESS_TOKEN'])

    # Use `client` to get 10 threads "from" lars@metafoo.de and store them in a
    # variable

    # Print out the subject of each of those threads

    # Send a message to inboxapptest415@gmail.com. The body should include all
    # message_ids of the 10 threads from above, each separated by a ",".

    # Print the raw RFC-2822 Message-ID Header in the message you just sent

if __name__ == '__main__':
    main()
