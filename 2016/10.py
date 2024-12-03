import file_helpers


def part1():
    class Output:
        def __init__(self, output_no):
            self.output_no = output_no
            self.values = []

        def add_value(self, val):
            self.values.append(val)

    class Bot:
        def __init__(self, bot_no):
            self.values = []
            self.bot_no = bot_no
            self.low_target = None
            self.high_target = None

        def add_value(self, value):
            self.values.append(value)
            self.values = sorted(self.values)
            if len(self.values) == 2 and self.values[0] == 17 and self.values[1] == 61:
                print(f"bot {self.bot_no} holds 17 and 61")
            if len(self.values) == 2:
                low = self.values.pop(0)
                self.low_target.add_value(low)
                high = self.values.pop(0)
                self.high_target.add_value(high)

    def get_or_create_bot(number):
        if number not in bots:
            bots[number] = Bot(number)
        return bots[number]

    def get_or_create_output(number):
        if number not in outputs:
            outputs[number] = Output(number)
        return outputs[number]

    bots = {}
    outputs = {}

    for l in file_helpers.get_all_lines("inputs/10.txt"):
        parts = l.split(' ')
        if parts[0] == "bot":
            bot = get_or_create_bot(parts[1])
            if parts[5] == 'bot':
                bot.low_target = get_or_create_bot(parts[6])
            else:
                bot.low_target = get_or_create_output(parts[6])
            if parts[10] == 'bot':
                bot.high_target = get_or_create_bot(parts[11])
            else:
                bot.high_target = get_or_create_output(parts[11])

    for l in file_helpers.get_all_lines("inputs/10.txt"):
        parts = l.split(' ')
        if parts[0] == 'value':
            value = int(parts[1])
            bot = parts[5]
            get_or_create_bot(bot).add_value(value)

    zero = get_or_create_output("0")
    one = get_or_create_output("1")
    two = get_or_create_output("2")
    print(zero.values[0] * one.values[0] * two.values[0])


part1()
