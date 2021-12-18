"""
Advent of Code 2021 | Day 15 | Part 2
"""
import sys
import heapq
import math


with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]

rows, cols = len(grid), len(grid[0])
dist = [[math.inf] * (5 * cols) for _ in range(5 * rows)]
dist[0][0] = 0

heap = [(0, 0)]

while heap:
    r, c = heapq.heappop(heap)

    if (r, c) == (5 * rows - 1, 5 * cols - 1):
        print(dist[r][c])
        break

    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        r_new, c_new = r + dr, c + dc
        if 0 <= r_new < 5 * rows and 0 <= c_new < 5 * cols:
            edge = grid[r_new % rows][c_new % cols] + r_new // rows + c_new // cols
            if edge > 9:
                edge %= 9
            if dist[r][c] + edge < dist[r_new][c_new]:
                dist[r_new][c_new] = dist[r][c] + edge
                heapq.heappush(heap, (r_new, c_new))
