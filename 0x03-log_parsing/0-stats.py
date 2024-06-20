#!/usr/bin/python3
"""Log parsing"""

import sys


def print_logs(status_codes, file_size):
    """Prints the logs"""
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{:s}: {:d}".format(key, value))

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            file_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
        if counter == 10:
            print_logs(status_codes, file_size)
            counter = 0
except KeyboardInterrupt:
    print_logs(status_codes, file_size)
    raise KeyboardInterrupt

print_logs(status_codes, file_size)

