#!/usr/bin/python3
"""Solves the N-Queens problem"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen on the given board position.

    Args:
        board (list): The current state of the board.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        N (int): The size of the board (N x N).

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, N, solutions):
    """
    Recursively solve the N-Queens problem.

    Args:
        board (list): The current state of the board.
        row (int): The current row being processed.
        N (int): The size of the board (N x N).
        solutions (list): The list to store the solutions.
    """
    if row == N:
        # All queens have been placed, add the current board state to the solutions list
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place a queen in the current row and column
            board[row] = col
            # Recursively solve the problem for the next row
            solve_n_queens_util(board, row + 1, N, solutions)


def nQueens():
    """
    Solve the N-Queens problem and print the solutions.
    """
    if len(sys.argv) != 2:
        print('Usage: nqueens N\n', file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number\n', file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print('N must be at least 4\n', file=sys.stderr)
        sys.exit(1)

    solutions = []
    solve_n_queens_util([-1] * N, 0, N, solutions)

    for sol in solutions:
        print([[i, col] for i, col in enumerate(sol)])

    sys.exit(0)


if __name__ == "__main__":
    nQueens()