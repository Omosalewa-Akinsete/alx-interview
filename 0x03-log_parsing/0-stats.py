#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict

total_size = 0
status_count = defaultdict(int)
line_count = 0

try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        try:
            _, _, _, _, status_code_str, file_size_str = line.split()
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except (ValueError, IndexError):
            continue

        total_size += file_size
        status_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print(f"Total file size: File size: {total_size}")
            for status_code in sorted(status_count):
                print(f"{status_code}: {status_count[status_code]}")

except KeyboardInterrupt:
    print(f"Total file size: File size: {total_size}")
    for status_code in sorted(status_count):
        print(f"{status_code}: {status_count[status_code]}")
