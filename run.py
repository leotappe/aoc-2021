import argparse
import os
import subprocess


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('part', type=int)
    parser.add_argument('--example', action='store_true')

    args = parser.parse_args()

    if not (1 <= args.day <= 24):
        print('Please specify a day between 1 and 24.')
        exit()

    if args.part not in {1, 2}:
        print('Please specify a part in {1, 2}.')
        exit()

    directory = f'day-{args.day:02d}'
    code = f'part_{args.part}.py'
    infile = 'example.txt' if args.example else 'input.txt'

    code_path = os.path.join(directory, code)
    input_path = os.path.join(directory, infile)

    if not os.path.exists(code_path):
        print(f'No code found at {code_path}.')
        exit()

    if not os.path.exists(input_path):
        print(f'No input found at {input_path}.')
        exit()

    subprocess.run(['python', code_path, input_path])
