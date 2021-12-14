"""
Advent of Code 2021 | Day 4 | Part 2
"""
import sys


def update(grid, drawn):
    for row in grid:
        for i, number in enumerate(row):
            if number == drawn:
                row[i] = -1


def has_bingo(grid):
    return any(all(x == -1 for x in row) for row in grid) or any(all(row[i] == -1 for row in grid) for i, _ in enumerate(grid[0]))


def score(grid, drawn):
    return drawn * sum(sum(x for x in row if x != -1) for row in grid)


def main():
    with open(sys.argv[1]) as f:
        drawn_numbers = [int(x) for x in f.readline().split(',')]

        f.readline()

        grids = []

        grid = []

        while True:
            line = f.readline()


            if line in ['', '\n']:
                grids.append(grid)
                grid = []

                if line == '':
                    break
                continue

            grid.append([int(x) for x in line.split()])

    for number in drawn_numbers:
        new_grids = []

        for grid in grids:
            update(grid, number)
            if has_bingo(grid):
                if len(grids) == 1:
                    print(score(grid, number))
                    return
            else:
                new_grids.append(grid)
        
        grids = new_grids


if __name__ == '__main__':
    main()
