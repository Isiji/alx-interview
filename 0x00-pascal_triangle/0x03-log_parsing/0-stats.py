#!/usr/bin/python3

import sys

def print_stats(status_codes, file_size):
    """Print stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
    