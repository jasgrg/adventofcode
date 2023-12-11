from file_helpers import open_file, get_next_line


def calculate_next_value(nums):
    if len([n for n in nums if n != 0]) == 0:
        return 0

    diffs = []
    for idx in range(0, len(nums) - 1):
        diffs.append(nums[idx + 1] - nums[idx])

    return nums[0] - calculate_next_value(diffs)


def go():
    open_file("assets/09.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        nums = [int(a) for a in l.split(' ')]
        total += calculate_next_value(nums)
        line_number, l, eof = get_next_line()
    print(str(total))
