"""
Advent of Code 2021 | Day 11 | Part 1
"""
import sys


with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]


def step(grid):
    charged = set()
    flashed = set()

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] += 1
            if grid[i][j] > 9:
                charged.add((i, j))
    
    num_flashes = 0
    while charged:
        i, j = charged.pop()
        flashed.add((i, j))
        num_flashes += 1
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                if 0 <= i + di < 10 and 0 <= j + dj < 10:
                    grid[i + di][j + dj] += 1
                    if grid[i + di][j + dj] > 9 and (i + di, j + dj) not in charged | flashed:
                        charged.add((i + di, j + dj))
        
        for i, j in flashed:
            grid[i][j] = 0

    return num_flashes


flashes = 0

for _ in range(100):
    flashes += step(grid)
    
print(flashes)
