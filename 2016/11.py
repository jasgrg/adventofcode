import itertools


def part1():
    def eval(step_floors):
        return len(step_floors[3]) * 10 + len(step_floors[2]) * 2 + len(step_floors[1]) * 0

    def are_equal(left, right):
        for floor in range(4):
            if len(left[floor]) != len(right[floor]) or \
                    len([p for p in left[floor] if len([q for q in right[floor] if q.equals(p)]) > 0]) != len(left):
                return False
        return True

    def is_repeat(f, history):
        for h in history:
            if are_equal(f, h):
                return True
        return False

    def print_steps(location, step_cnt, step_floors):
        print(f"{step_cnt})")
        for i in range(len(floors)):
            floor = len(floors) - 1 - i
            desc = f"F{floor + 1}"
            if floor == location:
                desc += " E"
            for p in step_floors[floor]:
                desc += f" {p.element[0:1]}{p.type[0:1]}"
            print(desc)
        print("")

    def is_end_state(step_floors):
        return len(step_floors[0]) == 0 and \
            len(step_floors[1]) == 0 and \
            len(step_floors[2]) == 0

    def is_valid_floor(floor):
        for part in floor:
            if part.type == "microchip":
                if len([x for x in floor if x.element == part.element and x.type == "generator"]) == 0:
                    if len([x for x in floor if x.element != part.element and x.type == "generator"]) > 0:
                        return False
        return True

    def is_valid(step_floors):
        for f in step_floors:
            if not is_valid_floor(f):
                return False
        return True

    def copy_floors(step_floors):
        return [[p for p in f] for f in step_floors]

    class Part:
        def __init__(self, element, type):
            self.element = element
            self.type = type

        def equals(self, other):
            return self.element == other.element and self.type == other.type

    def move_elements(step_floors, floor_number, elements, target_floor):

        new_floors = copy_floors(step_floors)
        for p in elements:
            new_floors[floor_number] = [prt for prt in new_floors[floor_number] if
                                        not (prt.type == p.type and prt.element == p.element)]
            new_floors[target_floor].append(p)
        return new_floors

    def get_possible_steps(location, step_cnt, step_floors, history):
        possible_steps = []
        parts = [[p] for p in step_floors[location]]
        can_move_down = False
        for floor_indx in range(location):
            if len(step_floors[floor_indx]) > 0:
                can_move_down = True
                break

        for p in parts:
            if location > 0:
                if can_move_down:
                    new_floors = move_elements(step_floors, location, p, location - 1)
                    if is_end_state(new_floors):
                        print(step_cnt + 1)
                        exit(0)
                    if not is_repeat(new_floors, history):
                        if is_valid(new_floors):
                            possible_steps.append(
                                (location - 1, step_cnt + 1,
                                 new_floors, history + [new_floors], eval(new_floors)))
                    else:
                        print('here')
        parts = parts + [c for c in itertools.combinations(step_floors[location], 2)]
        for p in parts:
            if location < len(floors) - 1:
                new_floors = move_elements(step_floors, location, p, location + 1)
                if is_end_state(new_floors):
                    print(step_cnt + 1)
                    exit(0)
                if not is_repeat(new_floors, history):
                    if is_valid(new_floors):
                        possible_steps.append(
                            (location + 1, step_cnt + 1,
                             new_floors, history + [new_floors], eval(new_floors)))
                else:
                    print('here')
        return possible_steps

    #
    # floors = [
    #     [Part("hydrogen", "microchip"), Part("lithium", "microchip")],
    #     [Part("hydrogen", "generator")],
    #     [Part("lithium", "generator")],
    #     []
    # ]

    floors = [
        [Part("thulium", "generator"), Part("thulium", "microchip"), Part("plutonium", "generator"),
         Part("strontium", "generator")
         ],
        [Part("plutonium", "microchip"), Part("strontium", "microchip")],
        [Part("promethium", "generator"), Part("promethium", "microchip"), Part("ruthenium", "generator"),
         Part("ruthenium", "microchip")],
        []
    ]
    steps = get_possible_steps(0, 0, floors, [])
    previous_stp_cnt = 0
    history = []
    while len(steps) > 0:

        step = steps.pop(0)
        history.append(step[2])
        # print_steps(step[0], step[1], step[2])
        if previous_stp_cnt != step[1]:
            print(f"{step[1]} - {len(steps)}")
            previous_stp_cnt = step[1]

        # print_steps(step[0], step[1], step[2])
        steps += get_possible_steps(step[0], step[1], step[2], step[3])
        # steps = sorted(sorted(steps, key=lambda s: s[4], reverse=True), key=lambda s: s[1])


part1()
