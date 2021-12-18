"""
Advent of Code 2021 | Day 14 | Part 2
"""
import sys
import collections
import string


with open(sys.argv[1]) as f:
    template = list(f.readline().strip())
    f.readline()
    rules = {}

    while True:
        line = f.readline()
        if not line:
            break
        pair, insert = line.strip().split(' -> ')
        rules[pair] = insert

elements = set(template) | set(''.join(rules.keys())) | set(''.join(rules.values()))
cache = {}

def count(left, right, target, steps):
    if (left, right, target, steps) not in cache:
        if steps == 0 or left + right not in rules:
            cache[(left, right, target, steps)] = 0
        else:
            new = rules[left + right]
            cache[(left, right, target, steps)] = count(left, new, target, steps - 1) + count(new, right, target, steps - 1) + (target == new)
    return cache[(left, right, target, steps)]

counter = collections.Counter(template)

for left, right in zip(template[:-1], template[1:]):
    for element in elements:
        counter[element] += count(left, right, element, 40)

counts = [c for _, c in counter.most_common()]
print(counts[0] - counts[-1])
