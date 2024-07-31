#!/usr/bin/python3
"""Solves the N-Queens problem"""
import sys


def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N, board, col, solutions):
    if col == N:
        solutions.append([queens[:] for queens in board])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(N, board, col + 1, solutions)
            board[i][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        print("[", end="")
        for i in range(len(solution)):
            print("[", end="")
            for j in range(len(solution)):
                if solution[i][j] == 1:
                    print("1", end="")
                else:
                    print("0", end="")
                if j < len(solution) - 1:
                    print(", ", end="")
            print("]", end="")
            if i < len(solution) - 1:
                print(", ", end="")
        print("]")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)
