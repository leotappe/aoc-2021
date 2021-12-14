"""
Advent of Code 2021 | Day 2 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    instructions = f.readlines()

horizontal_pos = 0
depth = 0
aim = 0

for instruction in instructions:
    direction, x = instruction.split()
    x = int(x)

    if direction == 'forward':
        horizontal_pos += x
        depth += aim * x
    elif direction == 'up':
        aim -= x
    else:
        aim += x

print(horizontal_pos * depth)
