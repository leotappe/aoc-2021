"""
Advent of Code 2021 | Day 8 | Part 1
"""
import sys


def solve(signal_patterns, output_values):
    return len([val for val in output_values if len(val) in {2, 3, 4, 7}])

with open(sys.argv[1]) as f:
    lines = [line.strip().split('|') for line in f.readlines()]

sol = 0

for first, second in lines:
    input_patterns = first.strip().split(' ')
    output_values = second.strip().split(' ')
    sol += solve(input_patterns, output_values)

print(sol)
