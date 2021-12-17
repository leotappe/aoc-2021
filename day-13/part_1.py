"""
Advent of Code 2021 | Day 13 | Part 1
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
    
    break

print(len(coordinates))
