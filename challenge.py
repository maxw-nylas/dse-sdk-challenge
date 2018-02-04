#!/usr/bin/env python
from nylas import APIClient
import json

config = json.load(open('config.json'))

def main():
    client = APIClient(config['NYLAS_APP_ID'], config['NYLAS_APP_SECRET'], config['NYLAS_ACCESS_TOKEN'])

    # Get 10 threads from lars@metafoo.de

    # Print out the subject of each of those threads

    # Send a message to mike@nylas.com. The body should include all message_ids of
    # the threads from above. 

    # Print the Message-ID Header in the message you just sent

if __name__ == '__main__':
    main()
