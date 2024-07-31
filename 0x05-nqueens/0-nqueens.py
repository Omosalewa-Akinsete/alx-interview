#!/usr/bin/python3
"""Solves the N-Queens problem"""
import sys

if __name__ == '__main__':
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        # Try to parse the value of N from the command-line argument
        n = int(sys.argv[1])
    except ValueError:
        # If the value of N is not an integer, print an error message and exit
        print('N must be a number')
        sys.exit(1)

    # If the value of N is less than 4, print an error message and exit
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)