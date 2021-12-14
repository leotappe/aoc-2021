"""
Advent of Code 2021 | Day 6 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    values = [int(x) for x in f.readline().strip().split(',')]

cache = {}

def simulate(value, days_left):
    if (value, days_left) not in cache:
        if value >= days_left:
            cache[(value, days_left)] = 1
        else:
            cache[(value, days_left)] = simulate(6, days_left - value - 1) + simulate(8, days_left - value - 1)
    return cache[(value, days_left)]


print(sum(simulate(value, 256) for value in values))
