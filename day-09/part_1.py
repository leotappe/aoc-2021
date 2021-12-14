"""
Advent of Code 2021 | Day 9 | Part 1
"""
import sys


def is_low_point(grid, r, c):
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[r + dr]) and grid[r][c] >= grid[r + dr][c + dc]:
            return False

    return True


with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]

sol = 0

for r, row in enumerate(grid):
    for c, height in enumerate(row):
        if is_low_point(grid, r, c):
            sol += height + 1

print(sol)
