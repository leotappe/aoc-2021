"""
Advent of Code 2021 | Day 13 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    lines = f.readlines()


coordinates = set()
instructions = []

for line in lines:
    if line == '\n':
        continue
    if ',' in line:
        x, y = [int(s) for s in line.strip().split(',')]
        coordinates.add((x, y))
    else:
        _, _, fold = line.split(' ')
        axis, value = fold.split('=')
        instructions.append((axis, int(value)))

for axis, value in instructions:
    if axis == 'x':
        right_of_axis = {(x, y) for x, y in coordinates if x > value}
        coordinates -= right_of_axis
        for x, y in right_of_axis:
            coordinates.add((2 * value - x, y))
    else:
        below_axis = {(x, y) for x, y in coordinates if y > value}
        coordinates -= below_axis
        for x, y in below_axis:
            coordinates.add((x, 2 * value - y))

x_max = max(x for x, _ in coordinates)
x_min = min(x for x, _ in coordinates)
y_max = max(y for _, y in coordinates)
y_min = min(y for _, y in coordinates)

grid = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

for x, y in coordinates:
    grid[y - y_min][x - x_min] = '#'

for row in grid:
    print(''.join(row))