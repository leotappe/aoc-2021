"""
Advent of Code 2021 | Day 9 | Part 2
"""
import sys
import heapq


def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 9:
        return 0

    grid[r][c] = 9
    return 1 + sum(dfs(grid, r + dr, c + dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)])


with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]

heap = []

for r, row in enumerate(grid):
    for c, height in enumerate(row):
        heapq.heappush(heap, -dfs(grid, r, c))

sol = 1

for _ in range(3):
    sol *= -heapq.heappop(heap)

print(sol)
