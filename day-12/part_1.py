"""
Advent of Code 2021 | Day 12 | Part 1
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
    return all(c in string.ascii_lowercase for c in u)

def find_all_paths(u, adj, visited, sol):
    if u == 'end':
        return sol + 1

    if small(u):
        visited.add(u)

    for v in adj[u]:
        if v != 'start' and v not in visited:
            sol = find_all_paths(v, adj, visited, sol)
    
    if small(u):
        visited.remove(u)
    return sol

print(find_all_paths('start', adj, set(), 0))
