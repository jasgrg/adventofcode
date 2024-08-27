from utlities import LETTERS

# part 1:
# pword = list('hxbxwxba')

# part 2:
pword = list('hxbxxyzz')


def go():
    test = 0
    while True:
        test += 1
        if test > 1000000:
            test = 0
            print(''.join(pword))
        increment(pword)

        if is_valid(pword):
            break
    print("found this after " + str(test) + " tries : " + ''.join(pword))


def is_valid(word):
    if 'i' in word or 'o' in word or 'l' in word:
        return False
    idx = 0
    pairs_found = 0
    run_found = False

    while idx < len(word) - 1:
        if word[idx] == word[idx + 1]:
            pairs_found += 1
            idx += 1
        idx += 1
    if pairs_found < 2:
        return False
    idx = 0
    while idx < len(word) - 1:
        if idx < len(word) - 2:
            value = find_letter_value(word[idx])
            if value < len(LETTERS) - 2:
                if word[idx + 1] == LETTERS[value + 1] and word[idx + 2] == LETTERS[value + 2]:
                    run_found = True
                    idx += 2
        idx += 1
    return run_found


def increment(word):
    idx = len(word) - 1
    while idx >= 0:
        value = find_letter_value(word[idx])
        value += 1
        if value >= len(LETTERS):
            value = 0
            word[idx] = LETTERS[value]
            idx -= 1
        else:
            word[idx] = LETTERS[value]
            break


def find_letter_value(letter):
    for idx, l in enumerate(LETTERS):
        if l == letter:
            return idx
