"""
Advent of Code 2021 | Day 6 | Part 1

2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0
      1             1             1             1             1           
                        1             2             3             4
                                          1             3             6
                                                            1             4

Sure does look like Pascal's triangle...    
"""
import sys


with open(sys.argv[1]) as f:
    values = [int(x) for x in f.readline().strip().split(',')]

def simulate(value, days_left):
    if value >= days_left:
        return 1
    return simulate(6, days_left - value - 1) + simulate(8, days_left - value - 1)

print(sum(simulate(value, 80) for value in values))
