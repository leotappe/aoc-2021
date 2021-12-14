"""
Advent of Code 2021 | Day 7 | Part 1
"""
import sys
import math
import statistics


with open(sys.argv[1]) as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

align_at = math.ceil(statistics.median(positions))
print(sum(abs(p - align_at) for p in positions))
