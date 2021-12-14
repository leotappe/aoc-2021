"""
Advent of Code 2021 | Day 10 | Part 1
"""
import sys


with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

score = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def find_first_illegal(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif not stack:
            return None
        elif stack[-1] == match[c]:
            stack.pop()
        else:
            return c

print(sum(score[find_first_illegal(line)] for line in lines))
