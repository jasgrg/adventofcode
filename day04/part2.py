from file_helpers import get_all_lines


def go():
    total = 0
    lines = get_all_lines("assets/4_scratchcards.txt")
    card_counts = [1 for m in range(0, len(lines))]
    for idx, l in enumerate(lines):
        parts = l.split(':')
        sides = parts[1].split('|')

        winning_numbers = [int(s) for s in sides[0].split(' ') if s != '']
        my_numbers = [int(s) for s in sides[1].split(' ') if s != '']
        matches = [m for m in my_numbers if m in winning_numbers]

        for c in range(idx + 1, idx + 1 + len(matches)):
            card_counts[c] += card_counts[idx]
    for c in card_counts:
        total += c
    print(total)
