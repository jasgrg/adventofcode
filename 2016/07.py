import utlities
from file_helpers import get_all_lines


def part1():
    def is_abba(s):
        return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

    cnt = 0
    for l in get_all_lines("inputs/07.txt"):
        in_bracket = False
        abba_in = False
        abba_out = False
        for indx in range(len(l) - 3):
            if l[indx] == '[':
                in_bracket = True
            elif l[indx] == ']':
                in_bracket = False
            else:
                abba = is_abba(l[indx: indx + 4])
                if abba and in_bracket:
                    abba_in = True
                if abba and not in_bracket:
                    abba_out = True
        cnt += 1 if abba_out and not abba_in else 0
    print(cnt)


def part2():
    def is_aba(s):
        return s[0] == s[2] and s[1] != s[0]

    def contains_bab(aba, str):
        bab = aba[1] + aba[0] + aba[1]
        return bab in str

    cnt = 0
    for l in get_all_lines("inputs/07.txt"):
        inside = ' '.join(utlities.regex_findall(l, '\[(.*?)\]'))
        outside = ' '.join(utlities.regex_findall(l, '([^[\]]+)(?:\[[^\]]*\])*'))
        for indx in range(len(outside) - 2):
            if is_aba(outside[indx: indx + 3]):
                if contains_bab(outside[indx: indx + 3], inside):
                    cnt += 1
                    break
    print(cnt)


part2()
