#!/usr/bin/python3
"""
    this script reads from stdin line by line and computes metrics
"""


import sys
import re
import signal


total_size = 0
result = {}


def display_metrics():
    """displays the metrics information in a format"""
    print("File size: {}".format(total_size))
    for key in sorted(result):
        print("{}: {}".format(key, result[key]))


def sigint_handler(signum, frame):
    """handles a sigint signal"""
    display_metrics()
    exit(1)


signal.signal(signal.SIGINT, sigint_handler)
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
log_entry_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET ([^"]+)" (\d+) (\d+)'


for line in sys.stdin:
    if count == 10:
        count = 1
        display_metrics()
    else:
        count += 1

    match = re.match(log_entry_pattern, line)
    if match:
        line = match.groups()
        status_code, file_size = line[-2], line[-1]
        if status_code in valid_codes:
            try:
                total_size += int(file_size)
                if status_code not in result:
                    result[status_code] = 1
                else:
                    result[status_code] += 1
            except Exception as e:
                pass

display_metrics()
