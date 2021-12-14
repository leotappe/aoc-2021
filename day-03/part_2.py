"""
Advent of Code 2021 | Day 3 | Part 2
"""
import sys


with open(sys.argv[1]) as f:
    numbers = [line.rstrip() for line in f.readlines()]


# oxygen generator rating
remaining = numbers
index = -1

while len(remaining) > 1:
    index += 1
    zeros = []
    ones = []

    for number in remaining:
        if (number[index] == '0'):
            zeros.append(number)
        else:
            ones.append(number)

    if len(ones) >= len(zeros):
        remaining = ones
    else:
        remaining = zeros

oxygen_generator_rating = int(remaining[0], base=2)


# CO2 scrubber rating
remaining = numbers
index = -1

while len(remaining) > 1:
    index += 1
    zeros = []
    ones = []

    for number in remaining:
        if (number[index] == '0'):
            zeros.append(number)
        else:
            ones.append(number)

    if len(zeros) <= len(ones):
        remaining = zeros
    else:
        remaining = ones

co2_scrubber_rating = int(remaining[0], base=2)

print(oxygen_generator_rating * co2_scrubber_rating)
