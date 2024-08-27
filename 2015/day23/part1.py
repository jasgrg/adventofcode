from file_helpers import open_file, get_next_line


class Instruction:
    def __init__(self, inst, reg, value):
        self.inst = inst
        self.reg = reg
        self.value = int(value) if value is not None else None


def go():
    registers = {
        'a': 0,
        'b': 0
    }

    instructions = []

    open_file("assets/23.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        parts = l.split(' ')
        inst = parts[0]
        parts[1] = parts[1].replace(',', '').replace('+', '')
        reg = None
        value = None
        if parts[1] in ['a', 'b']:
            reg = parts[1]
            if len(parts) > 2:
                value = parts[2].replace('+', '')
        else:
            value = parts[1]
        instructions.append(Instruction(inst, reg, value))

    inst_index = 0
    while inst_index < len(instructions):
        inst = instructions[inst_index]
        if inst.inst == 'inc':
            registers[inst.reg] += 1
        elif inst.inst == 'jio':
            if registers[inst.reg] == 1:
                inst_index += inst.value
                continue
        elif inst.inst == 'hlf':
            registers[inst.reg] /= 2
        elif inst.inst == 'tpl':
            registers[inst.reg] *= 3
        elif inst.inst == 'jmp':
            inst_index += inst.value
            continue
        elif inst.inst == 'jie':
            if registers[inst.reg] % 2 == 0:
                inst_index += inst.value
                continue
        else:
            print(f"bad instruction {inst.inst}")
        inst_index += 1
    print(f"{registers['b']}")
