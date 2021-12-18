"""
Advent of Code 2021 | Day 15 | Part 1
"""
import sys
import heapq
import math


with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]

rows, cols = len(grid), len(grid[0])
dist = [[math.inf] * cols for _ in range(rows)]
dist[0][0] = 0

heap = [(0, 0)]

while heap:
    r, c = heapq.heappop(heap)

    if (r, c) == (rows - 1, cols - 1):
        print(dist[r][c])
        break

    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if 0 <= r + dr < rows and 0 <= c + dc < cols and dist[r][c] + grid[r + dr][c + dc] < dist[r + dr][c + dc]:
            dist[r + dr][c + dc] = dist[r][c] + grid[r + dr][c + dc]
            heapq.heappush(heap, (r + dr, c + dc))
