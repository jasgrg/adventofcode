from random import randrange

from file_helpers import open_file, get_next_line


class Transition:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Pass:
    def __init__(self, count, value):
        self.count = count
        self.value = value


transitions = []


def go():
    global transitions
    open_file("assets/19.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof or l == '':
            break

        parts = l.split(' ')
        transitions.append(Transition(parts[0], parts[2]))
    line_number, molecule, eof = get_next_line()

    transitions = sorted(transitions, key=lambda x: len(x.value), reverse=True)

    new_molecule = molecule
    min_transaction_count = 999999999
    transition_cnt = 0
    remaining_transitions = transitions
    while True:
        prev_molecule = new_molecule
        t, remaining_transitions = get_next_transition(remaining_transitions)
        new_molecule = new_molecule.replace(t.value, t.key, 1)
        if new_molecule != prev_molecule:
            transition_cnt += 1
            remaining_transitions = transitions

        if new_molecule == 'e':
            if min(transition_cnt, min_transaction_count) != min_transaction_count:
                print(f"found new min {transition_cnt}")
            min_transaction_count = min(min_transaction_count, transition_cnt)
            transition_cnt = 0
            remaining_transitions = transitions
            new_molecule = molecule

        if len(remaining_transitions) == 0:
            # print(f"cannot find additional replacements {new_molecule}")
            remaining_transitions = transitions
            transition_cnt = 0
            new_molecule = molecule


def get_next_transition(transitions):
    index = randrange(len(transitions))
    new_transitions = [t for t in transitions if t.value != transitions[index].value]
    return transitions[index], new_transitions
