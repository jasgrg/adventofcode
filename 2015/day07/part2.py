from file_helpers import open_file, get_next_line
from utlities import is_numeric

max = 65535

wires = {}


def any_left_unset():
    for w in wires:
        if not w.set:
            return True
    return False


def forward_value(wire):
    for w in wires:
        if w.left == wire.target_wire:
            w.left_value = wire.value
        if w.right == wire.target_wire:
            w.right_value = wire.value


class Gate:
    def __init__(self, target_wire, operand, left, right):
        self.target_wire = target_wire
        self.operand = operand
        self.left = left
        self.left_value = None
        self.right_value = None
        self.right = right
        self.value = None
        self.set = False
        if self.right is not None and is_numeric(self.right):
            self.right_value = int(self.right)
        if self.left is not None and is_numeric(self.left):
            self.left_value = int(self.left)

    def try_set(self):
        if self.operand == 'SET':
            if self.left_value is not None:
                self.value = self.left_value
                self.set = True
            elif is_numeric(self.left):
                self.value = int(self.left)
                self.set = True
        if self.operand == 'NOT' and self.left_value is not None:
            self.value = bit_not(self.left_value)
            self.set = True
        if self.operand == 'AND' and self.left_value is not None and self.right_value is not None:
            self.value = self.left_value & self.right_value
            self.set = True
        if self.operand == 'OR' and self.left_value is not None and self.right_value is not None:
            self.value = self.left_value | self.right_value
            self.set = True
        if self.operand == 'LSHIFT' and self.left_value is not None and self.right_value is not None:
            self.value = self.left_value << int(self.right)
            self.set = True
        if self.operand == 'RSHIFT' and self.left_value is not None and self.right_value is not None:
            self.value = self.left_value >> int(self.right)
            self.set = True
        if self.set:
            print(str(self.value) + " => " + self.target_wire)


def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n


def get_wire(wire):
    for w in wires:
        if w.target_wire == wire:
            return w


def go():
    open_file("assets/07.txt")
    line_number, l, eof = get_next_line()
    global wires
    wires = []
    while not eof:
        sides = l.split(' -> ')
        target_wire = sides[1]
        tokens = sides[0].split(' ')
        if len(tokens) == 1:
            wires.append(Gate(target_wire, 'SET', tokens[0], None))

        if len(tokens) == 2:
            wires.append(Gate(target_wire, 'NOT', tokens[1], None))

        if len(tokens) == 3:
            left = tokens[0]
            op = tokens[1]
            right = tokens[2]
            wires.append(Gate(target_wire, op, left, right))
        line_number, l, eof = get_next_line()

    while any_left_unset():
        for w in wires:
            if not w.set:
                w.try_set()
                if w.set:
                    forward_value(w)

    a = get_wire('a')
    print(a.value)
