#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import signal


total_size = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) > 6:
        file_size = parts[-1]
        status_code = parts[-2]
        if status_code in status_counts:
            try:
                total_size += int(file_size)
                status_counts[status_code] += 1
            except ValueError:
                pass
    if line_count % 10 == 0:
        print_stats()

print_stats()
