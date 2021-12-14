"""
Advent of Code 2021 | Day 5 | Part 1
"""
import sys


class Line:
    def __init__(self, s):
        start, _, end = s.split(' ')
        x1, y1 = [int(z) for z in start.split(',')]
        x2, y2 = [int(z) for z in end.split(',')]
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


with open(sys.argv[1]) as f:
    lines = [Line(line.rstrip()) for line in f.readlines()]

x_max = max(max(line.x1 for line in lines), max(line.x2 for line in lines))
y_max = max(max(line.y1 for line in lines), max(line.y2 for line in lines))

grid = [[0] * (y_max + 1) for _ in range(x_max + 1)]

for line in lines:
    dx = (line.x2 - line.x1) // max(abs(line.x2 - line.x1), 1)
    dy = (line.y2 - line.y1) // max(abs(line.y2 - line.y1), 1)

    if min(abs(dx), abs(dy)) > 0:
        continue

    x, y = line.x1, line.y1

    while True:
        grid[x][y] += 1
        if (x, y) == (line.x2, line.y2):
            break
        x += dx
        y += dy

print(sum(sum(count >= 2 for count in row) for row in grid))
