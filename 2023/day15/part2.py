from file_helpers import open_file, get_next_line

boxes = []


class Lens:
    def __init__(self, label, power):
        self.label = label
        self.power = power


for i in range(0, 256):
    boxes.append([])


def remove_lens(box_no, label):
    boxes[box_no] = [l for l in boxes[box_no] if l.label != label]


def add_lens(box_no, lens: Lens):
    found = False
    for l in boxes[box_no]:
        if l.label == lens.label:
            l.power = lens.power
            found = True
    if not found:
        boxes[box_no].append(lens)


def get_box_no(label):
    box_no = 0
    for c in label:
        box_no += ord(c)
        box_no *= 17
        box_no = box_no % 256
    return box_no


def go():
    open_file("assets/15.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        lenses = l.split(',')

        for lense in lenses:
            if lense.endswith('-'):
                label = lense[0:len(lense) - 1]
                box_no = get_box_no(label)
                remove_lens(box_no, label)
            else:
                parts = lense.split('=')
                power = int(parts[1])
                label = parts[0]
                add_lens(get_box_no(label), Lens(label, power))

        line_number, l, eof = get_next_line()

    for index, box in enumerate(boxes):

        lense_value = 0
        for lense_index, l in enumerate(box):
            lense_value += (index + 1) * (lense_index + 1) * l.power
        total += lense_value
    print(total)
