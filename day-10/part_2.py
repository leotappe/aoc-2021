"""
Advent of Code 2021 | Day 10 | Part 2
"""
import sys
import statistics


with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]

match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def compute_score(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif not stack:
            # Should not happen
            return 0
        elif stack[-1] == match[c]:
            stack.pop()
        else:
            return 0

    score = 0
    while stack:
        score *= 5
        score += points[match[stack.pop()]]

    return score

print(statistics.median(s for line in lines if (s := compute_score(line)) > 0))
