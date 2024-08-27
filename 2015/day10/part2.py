def go():
    input = "1113222113"
    output = ""
    for i in range(50):
        while len(input) > 0:
            val, cnt, input = find_next_str(input)
            output += str(cnt) + val
        # print(output)
        input = output
        print(str(i))
        print(len(output))
        output = ""


def find_next_str(input):
    if len(input) == 1:
        return input[0], 1, ''

    val = input[0]
    input = input[1:]
    cnt = 1
    while input[0] == val:
        cnt += 1
        if len(input) == 1:
            break
        input = input[1:]
    return val, cnt, input
