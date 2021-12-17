"""
Advent of Code 2021 | Day 12 | Part 2
"""
import sys
import collections
import string


with open(sys.argv[1]) as f:
    edges = [line.strip().split('-') for line in f.readlines()]

adj = collections.defaultdict(list)

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

def small(u):
    return u != 'start' and u != 'end' and all(c in string.ascii_lowercase for c in u)

def find_all_paths(u, adj, visits, sol, special):
    if u == 'end':
        return sol + 1

    visits[u] += 1

    for v in adj[u]:
        if v == 'start':
            continue
        if not small(v) or visits[v] == 0 or (visits[v] == 1 and not special):
            if small(v) and visits[v] == 1:
                sol = find_all_paths(v, adj, visits, sol, True)
            else:
                sol = find_all_paths(v, adj, visits, sol, special)
    
    visits[u] -= 1
    return sol

print(find_all_paths('start', adj, collections.defaultdict(int), 0, False))
