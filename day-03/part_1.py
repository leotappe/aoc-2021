"""
Advent of Code 2021 | Day 3 | Part 1
"""
import sys


with open(sys.argv[1]) as f:
    binary_numbers = [line.rstrip() for line in f.readlines()]

num_numbers = len(binary_numbers)
num_digits = len(binary_numbers[0])

gamma = [False] * num_digits
epsilon = [False] * num_digits

for i in range(num_digits):
    count = sum(b[i] == '1' for b in binary_numbers)
    if count == num_numbers // 2:
        print('AMBIGUOUS')
    gamma[i] = count > num_numbers - count
    epsilon[i] = not gamma[i]


gamma = int(''.join(str(int(d)) for d in gamma), base=2)
epsilon = int(''.join(str(int(d)) for d in epsilon), base=2)

print(gamma * epsilon)
