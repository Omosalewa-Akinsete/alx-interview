#!/usr/bin/python3
"""The perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    grid: list of list of integers
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally)
        grid is rectangular, with its width and height not exceeding 100
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check each side of the cell
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1  # Top edge
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1  # Bottom edge
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1  # Left edge
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1  # Right edge

    return perimeter
