#!/usr/bin/python3
"""Solves the N-Queens problem"""
import sys


def n_queens(t_arr, col, i, n):
    """
       Find all possible solutions for N-queen problem
       and return them in a list
    """
    if i == n:
        t_arr.append(col[:])
        return t_arr

    for j in range(n):
        if all(j != col[k] and abs(j - col[k]) != i - k for k in range(i)):
            col[i] = j
            n_queens(t_arr, col, i + 1, n)

    return t_arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = n_queens([], [0] * n, 0, n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])
