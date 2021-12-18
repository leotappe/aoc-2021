"""
Advent of Code 2021 | Day 17 | Part 2
"""
import sys


def works(v_x, v_y, x_min, x_max, y_min, y_max):
    x, y = 0, 0

    while x <= x_max and y >= y_min:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        x += v_x
        y += v_y
        v_x = max(0, v_x - 1)
        v_y -= 1

    return False


def main():
    with open(sys.argv[1]) as f:
        _, bounds = f.readline().strip().split(': ')
        x_bounds, y_bounds = bounds.split(',')
        _, x_bounds = x_bounds.split('=')
        _, y_bounds = y_bounds.split('=')
        x_min, x_max = [int(c) for c in x_bounds.split('..')]
        y_min, y_max = [int(c) for c in y_bounds.split('..')]

    count = 0

    for v_x in range(x_max + 1):
        for v_y in range(y_min, -y_min):
            if works(v_x, v_y, x_min, x_max, y_min, y_max):
                count += 1

    print(count)


if __name__ == '__main__':
    main()
