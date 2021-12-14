"""
Advent of Code 2021 | Day 1 | Part 1
"""
import sys


with open(sys.argv[1]) as f:
    measurements = [int(line) for line in f.readlines()]

print(sum(nxt > curr for curr, nxt in zip(measurements[:-1], measurements[1:])))
