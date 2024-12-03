import file_helpers

input = file_helpers.read_all_text("inputs/09.txt")


def part1():
    indx = 0
    output = ''

    while indx < len(input):
        if input[indx] == "(":
            inner = ""
            indx += 1
            while input[indx] != ")":
                inner += input[indx]
                indx += 1
            indx += 1
            repeat = inner.split('x')
            length = int(repeat[0])
            times = int(repeat[1])
            for i in range(times):
                output += input[indx:indx + length]
            indx += length
        else:
            output += input[indx]
            indx += 1
    print(len(output))


def part2():
    def expand_substr(str):
        indx = 0
        substr_size = 0
        while indx < len(str):
            if str[indx] == "(":
                inner = ""
                indx += 1

                while str[indx] != ")":
                    inner += str[indx]
                    indx += 1
                indx += 1
                repeat = inner.split('x')
                length = int(repeat[0])
                times = int(repeat[1])
                substr_size += times * expand_substr(str[indx:indx + length])
                indx += length
            else:
                substr_size += 1
                indx += 1
        return substr_size

    print(expand_substr(input))


part2()
