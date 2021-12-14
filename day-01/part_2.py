"""
Advent of Code 2021 | Day 1 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    measurements = [int(line) for line in f.readlines()]

window_size = 3
window_sums = [sum(measurements[i:i + window_size]) for i in range(len(measurements) - window_size + 1)]

print(sum(nxt > curr for curr, nxt in zip(window_sums[:-1], window_sums[1:])))
