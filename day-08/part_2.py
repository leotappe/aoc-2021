"""
Advent of Code 2021 | Day 8 | Part 2
"""
import sys
import itertools


valid_digits = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

def solve(signal_patterns, output_values):
    for permutation in itertools.permutations('abcdefg'):
        if all(''.join(sorted(permutation[ord(c) - ord('a')] for c in pattern)) in valid_digits for pattern in signal_patterns):
            return int(''.join(valid_digits[''.join(sorted(permutation[ord(c) - ord('a')] for c in value))] for value in output_values))
    print('REEE')
    exit()

with open(sys.argv[1]) as f:
    lines = [[part.strip().split() for part in line.strip().split('|')] for line in f.readlines()]

print(sum(solve(first, second) for first, second in lines))
