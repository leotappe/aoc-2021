"""
Advent of Code 2021 | Day 14 | Part 1
"""
import sys
import collections


with open(sys.argv[1]) as f:
    template = list(f.readline().strip())
    f.readline()
    rules = collections.defaultdict(str)

    while True:
        line = f.readline()
        if not line:
            break
        pair, insert = line.strip().split(' -> ')
        rules[pair] = insert

def apply_rules(template, rules):
    inserted = [rules[cur + nxt] for cur, nxt in zip(template[:-1], template[1:])] + ['']
    return [element for old, new in zip(template, inserted) for element in (old, new)]

for _ in range(10):
    template = apply_rules(template, rules)

counts = [c for _, c in collections.Counter(template).most_common()]
print(counts[0] - counts[-1])
