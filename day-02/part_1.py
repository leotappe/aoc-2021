"""
Advent of Code 2021 | Day 2 | Part 1
"""
import sys


with open(sys.argv[1]) as f:
    instructions = f.readlines()

horizontal_pos = 0
depth = 0

for instruction in instructions:
    direction, x = instruction.split()
    x = int(x)

    if direction == 'forward':
        horizontal_pos += x
    elif direction == 'up':
        depth -= x
    else:
        depth += x

print(horizontal_pos * depth)
