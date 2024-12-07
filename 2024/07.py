from itertools import product

from file_helpers import get_all_lines

lines = get_all_lines("07.txt")


def calculate(operands):
    total = 0

    for l in lines:
        parts = l.split(':')
        val = int(parts[0])
        nums = [int(p) for p in parts[1].split(' ') if p != '']
        for c in product(operands, repeat=len(nums) - 1):

            test_val = nums[0]
            for idx in range(1, len(nums)):
                if c[idx - 1] == '+':
                    test_val += nums[idx]
                elif c[idx - 1] == '*':
                    test_val *= nums[idx]
                elif c[idx - 1] == '|':
                    test_val = int(f'{test_val}{nums[idx]}')
            if test_val == val:
                total += test_val
                break
    print(total)


# calculate(['+', '*'])
calculate('+*|')
