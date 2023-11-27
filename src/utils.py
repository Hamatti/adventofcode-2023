import os
import sys

def read_input(day, transformer=str, example=False):
    """
    Read puzzle input for file `/inputs/day_{day}.txt'
    and apply transformer function to each line.

    If `example` is set to True, read file `/inputs/day_{day}_example.txt`
    instead
    """

    try:
        if example:
            filename = f'day_{day}_example.txt'
        else:
            filename = f'day_{day}.txt'
        with open(os.path.join('..', 'inputs', filename)) as input_file:
            return [transformer(line) for line in input_file]
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

