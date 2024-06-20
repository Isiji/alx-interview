#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """Print the log stats"""
    print("File size: {:d}".format(total_file_size))
    for key, value in sorted(dict_sc.items()):
        print("{:s}: {:d}".format(key, value))