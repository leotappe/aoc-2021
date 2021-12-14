"""
Advent of Code 2021 | Day 7 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

def distance(p, q):
    d = abs(p - q)
    return d * (d + 1) // 2

print(min(sum(distance(p, q) for q in positions) for p in range(min(positions), max(positions) + 1)))
