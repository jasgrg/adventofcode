from file_helpers import open_file, get_next_line

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}


class Card:
    def calc_score(self):
        card_map = {
        }

        for c in self.hand:
            if c in card_map:
                card_map[c] += 1
            else:
                card_map[c] = 1
        jokers = 0 if 'J' not in card_map else card_map['J']
        card_map['J'] = 0
        if len([c for c in card_map if card_map[c] + jokers == 5]) > 0:
            return 600

        if len([c for c in card_map if card_map[c] + jokers >= 4]) > 0:
            return 500

        if len([c for c in card_map if card_map[c] == 3 or card_map[c] == 2]) == 2:
            if len([c for c in card_map if card_map[c] == 2]) == 2:
                if jokers > 0:
                    return 400
                return 200
            return 400
        if len([c for c in card_map if card_map[c] + jokers == 3]) > 0:
            return 300

        if len([c for c in card_map if card_map[c] == 2]) == 1:
            return 100
        if jokers > 0:
            return 100
        return 0

    def __lt__(self, other):
        if other.score['score'] == self.score['score']:
            for idx in range(0, len(self.hand)):
                if self.hand[idx] != other.hand[idx]:
                    return card_value[other.hand[idx]] < card_value[self.hand[idx]]

        return other.score['score'] < self.score['score']

    def __init__(self, hand, value):
        self.hand = hand
        self.value = value
        self.score = {
            'score': self.calc_score()
        }


def go():
    open_file("assets/7_cards.txt")
    line_number, l, eof = get_next_line()
    cards = []
    while not eof:
        parts = l.split(' ')
        cards.append(Card(parts[0], int(parts[1])))
        line_number, l, eof = get_next_line()
    cards.sort(reverse=True)

    total = 0
    for idx, c in enumerate(cards):
        total += (idx + 1) * c.value
    print(total)
