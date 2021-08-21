#!/usr/bin/python3

import requests
import time
import sys

URL = "http://151.216.12.5"
SLEEP = 4
PROGRAM = "unicorn.py"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

if len(sys.argv) > 1:
    PROGRAM = sys.argv[1]

def main():

    while True:
        print(f"Light program: {PROGRAM}")
        r = requests.post(
            URL,
            f"program={PROGRAM}",
            headers=HEADERS
        )
        print(f"Status code: {r.status_code}")
        print(f"Sleeping for: {SLEEP}")
        time.sleep(SLEEP)

if __name__=="__main__":
    main()
