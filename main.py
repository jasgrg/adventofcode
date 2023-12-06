# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def day4():
    with open('assets/4_scratchcards.txt') as f:
        lines = f.readlines()
        total = 0
        card_counts = [1 for x in range(0, len(lines))]
        for line_number, l in enumerate(lines):
            sides = l.split('|')
            winning_numbers = [int(a) for a in sides[0].split(':')[1].split(' ') if a != '']
            my_numbers = [int(a.replace('\n', '')) for a in sides[1].split(' ') if a != '']
            matched = [n for n in my_numbers if n in winning_numbers]
            if len(matched) > 0:
                score = pow(2, len(matched) - 1)
                total += score
                for c in range(line_number + 1, line_number + 1 + len(matched)):
                    card_counts[c] += card_counts[line_number]
        print(total)
        total = 0
        for c in card_counts:
            total += c
        print(total)
        # print(str(winning_numbers))


def day5_():
    class MapInfo:
        def __init__(self, target, source, rangeVal):
            self.dest_range_start = target
            self.dest_range_end = target + (rangeVal - 1)
            self.source_range_start = source
            self.source_range_end = source + (rangeVal - 1)
            self.rangeVal = rangeVal

        def isInRange(self, val):
            if val >= self.source_range_start and val <= self.source_range_end:
                return (val - self.source_range_start) + self.dest_range_start
            return -1

    class Maps:
        def __init__(self):
            self.maps = []

        def addMap(self, map):
            self.maps.append(map)

        def get_target(self, val):
            for m in self.maps:
                targetValue = m.isInRange(val)
                if targetValue >= 0:
                    return targetValue
            return val

    class SeedInfo:
        def __init__(self, seed):
            self.seed_number = seed
            self.soil = seed
            self.fertilizer = seed
            self.water = seed
            self.light = seed
            self.temp = seed
            self.humidity = seed
            self.location = seed

        def set_soil(self, value):
            self.soil = value
            self.fertilizer = value
            self.water = value
            self.light = value
            self.temp = value
            self.humidity = value
            self.location = value

        def set_fertilizer(self, value):
            self.fertilizer = value
            self.water = value
            self.light = value
            self.temp = value
            self.humidity = value
            self.location = value

        def set_water(self, value):
            self.water = value
            self.light = value
            self.temp = value
            self.humidity = value
            self.location = value

        def set_light(self, value):
            self.light = value
            self.temp = value
            self.humidity = value
            self.location = value

        def set_temp(self, value):
            self.temp = value
            self.humidity = value
            self.location = value

        def set_humidity(self, value):
            self.humidity = value
            self.location = value

        def set_location(self, value):
            self.location = value

    with open('assets/5_almanac.txt') as f:
        lines = f.readlines()
        total = 0
        card_counts = [1 for x in range(0, len(lines))]
        seeds = []
        line_number = 0
        for line_number in range(0, len(lines) - 1):
            l = lines[line_number].replace('\n', '')
            if l != '':
                if l.startswith("seeds"):
                    seed_vals = l.split(' ')[1:len(l.split(' '))]
                    # for seed_index in range(0, len(seed_vals), 2):
                    seed_start = int(seed_vals[0])
                    seed_range = int(seed_vals[1])
                    for seed_num in range(seed_start, seed_start + (seed_range - 1)):
                        seeds.append(SeedInfo(int(seed_num)))
                    print("initialized seeds " + str(seed_start))
                    # seed_start = int(seed_vals[seed_index])
                    # seed_range = int(seed_vals[seed_index + 1])
                    # for seed_num in range(seed_start, seed_start + (seed_range - 1)):
                    #     seeds.append(SeedInfo(int(seed_num)))
                    # print("initialized seeds " + seed_start)
                if l == 'seed-to-soil map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_soil(maps.get_target(s.seed_number))
                        # print('seed ' + str(s.seed_number) + ' goes to soil ' + str(s.soil))
                if l == 'soil-to-fertilizer map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_fertilizer(maps.get_target(s.soil))
                        # print('seed ' + str(s.seed_number) + ' goes to fertilizer ' + str(s.fertilizer))

                if l == 'fertilizer-to-water map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_water(maps.get_target(s.fertilizer))
                        # print('seed ' + str(s.seed_number) + ' goes to water ' + str(s.water))

                if l == 'water-to-light map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_light(maps.get_target(s.water))
                        # print('seed ' + str(s.seed_number) + ' goes to light ' + str(s.light))

                if l == 'light-to-temperature map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_temp(maps.get_target(s.light))
                        # print('seed ' + str(s.seed_number) + ' goes to temp ' + str(s.temp))

                if l == 'temperature-to-humidity map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        l = lines[line_number].replace('\n', '')
                    for s in seeds:
                        s.set_humidity(maps.get_target(s.temp))
                        # print('seed ' + str(s.seed_number) + ' goes to humidity ' + str(s.humidity))

                if l == 'humidity-to-location map:':
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        if (line_number != len(lines)):
                            l = lines[line_number].replace('\n', '')
                        else:
                            l = ''
                    for s in seeds:
                        s.set_location(maps.get_target(s.humidity))
                        # print('seed ' + str(s.seed_number) + ' goes to location ' + str(s.location))

        min_loc = -1
        for s in seeds:
            if min_loc == -1:
                min_loc = s.location
            elif s.location < min_loc:
                min_loc = s.location
        print(str(min_loc))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


from day05.part1 import go

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    go()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
