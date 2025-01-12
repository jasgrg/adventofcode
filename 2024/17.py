from file_helpers import get_all_lines
from utlities import bitwise_xor, bitwise_left_shift, bitwise_right_shift

lines = get_all_lines("input.txt")
a = int(lines[0].replace("Register A: ", ''))
b = int(lines[1].replace("Register B: ", ''))
c = int(lines[2].replace("Register C: ", ''))

code = [int(c) for c in lines[4].replace("Program: ", '').split(',')]


def part1(a):
    global b, c
    pointer = 0

    def get_combo_operand(op):
        if 0 <= op <= 3:
            return op
        if op == 4:
            return a
        if op == 5:
            return b
        if op == 6:
            return c
        else:
            raise Exception

    output = []
    while True:
        opcode = code[pointer]
        operand = code[pointer + 1]
        if opcode == 0:
            a = a // (pow(2, get_combo_operand(operand)))
        elif opcode == 1:
            b = bitwise_xor(b, operand)
        elif opcode == 2:
            b = get_combo_operand(operand) % 8
        elif opcode == 3:
            if a != 0:
                pointer = operand
                continue
        elif opcode == 4:
            b = bitwise_xor(b, c)
        elif opcode == 5:
            output.append(get_combo_operand(operand) % 8)
        elif opcode == 6:
            b = a // (pow(2, get_combo_operand(operand)))
        elif opcode == 7:
            c = a // (pow(2, get_combo_operand(operand)))
        pointer += 2
        if pointer >= len(code):
            break

    return output


def part2():
    # 2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0
    # b = a % 8
    # b = b xor 101
    # c = a / 2 ^ b
    # b = b xor 110
    # a = a / 2 ^ 3
    # b = b xor c
    # output += b % 8
    # repeat until a is 0

    a = 0
    postion = 1
    next_increment = 0
    while postion <= len(code):
        a = bitwise_left_shift(a, 3)
        for increment in range(next_increment, 8):
            if code[-postion:] == part1(a + increment):
                break
        else:
            postion -= 1
            a = bitwise_right_shift(a, 3)
            next_increment = a % 8 + 1
            a = bitwise_right_shift(a, 3)
            continue
        postion += 1
        a += increment
        next_increment = 0
    print(a)


# print(','.join(map(str, part1(a))))
print(part2())
