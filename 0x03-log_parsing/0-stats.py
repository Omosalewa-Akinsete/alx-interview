#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import re


def log_parsing():
    """
    Reads stdin line by line and computes metrics.
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    input_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '\
                    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    total_file_size = 0
    line_count = 0
    status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            match = re.match(input_pattern, line)
            if match:
                total_file_size += int(match.group(4))
                file_code = int(match.group(3))
                if file_code in status_code:
                    status_code[file_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stat(total_file_size, status_code)
        print_stat(total_file_size, status_code)
    except KeyboardInterrupt:
        print_stat(total_file_size, status_code)


def print_stat(total_file_size, status_code):
    print(f'File size: {total_file_size}')
    for code, count in sorted(status_code.items()):
        if count > 0:
            print(f'{code}: {count}')


if __name__ == "__main__":
    log_parsing()
