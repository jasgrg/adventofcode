def go():
    class SeedRange:
        def __init__(self, start, end, matched=False):
            self.range_start = start
            self.range_end = end
            self.matched = matched

    class MapInfo:
        def __init__(self, target, source, rangeVal):
            self.dest_range_start = target
            self.dest_range_end = target + (rangeVal - 1)
            self.source_range_start = source
            self.source_range_end = source + (rangeVal - 1)
            self.rangeVal = rangeVal
            self.delta = source - target

        def isInRange(self, seedRange):
            return seedRange.range_end >= self.source_range_start and \
                seedRange.range_start <= self.source_range_end

        def getNewRanges(self, seedRange: SeedRange):
            if seedRange.range_start >= self.source_range_start \
                    and seedRange.range_end <= self.source_range_end:
                return [SeedRange(seedRange.range_start - self.delta, seedRange.range_end - self.delta, True)]
            elif seedRange.range_start >= self.source_range_start and \
                    seedRange.range_start <= self.source_range_end \
                    and seedRange.range_end > self.source_range_end:
                return [SeedRange(seedRange.range_start - self.delta, self.source_range_end - self.delta, True),
                        SeedRange(self.source_range_end + 1, seedRange.range_end)]
            elif seedRange.range_start < self.source_range_start and \
                    seedRange.range_end >= self.source_range_start and seedRange.range_end <= self.source_range_end:
                return [SeedRange(seedRange.range_start, self.source_range_start - 1),
                        SeedRange(self.source_range_start - self.delta, seedRange.range_end - self.delta, True)]
            else:
                return [SeedRange(seedRange.range_start, self.source_range_start - 1),
                        SeedRange(self.source_range_start - self.delta, self.source_range_end - self.delta, True),
                        SeedRange(self.source_range_end + 1, seedRange.range_end)]

    class Maps:
        def __init__(self):
            self.maps = []

        def addMap(self, map):
            self.maps.append(map)

        def get_seed_ranges(self, seed_range: SeedRange):
            ranges = []
            for m in self.maps:
                if m.isInRange(seed_range):
                    for r in m.getNewRanges(seed_range):
                        if r.matched:
                            ranges.append(r)
                        else:
                            ranges += self.get_seed_ranges(r)
                    break
            if len(ranges) == 0:
                return [seed_range]

            return ranges

    with open('assets/5_almanac.txt') as f:
        lines = f.readlines()
        seeds = []
        line_number = 0
        while line_number < len(lines) - 1:
            l = lines[line_number].replace('\n', '')
            if l != '':
                if l.startswith("seeds"):
                    seed_vals = l.split(' ')[1:len(l.split(' '))]
                    for seed_index in range(0, len(seed_vals), 2):
                        seed_start = int(seed_vals[seed_index])
                        seed_range = int(seed_vals[seed_index + 1])
                        seeds.append(SeedRange(seed_start, seed_start + seed_range - 1))
                if l.endswith('map:'):
                    line_number += 1
                    l = lines[line_number].replace('\n', '')
                    maps = Maps()
                    while l != '':
                        nums = l.replace('\n', '').split(' ')
                        maps.addMap(MapInfo(int(nums[0]), int(nums[1]), int(nums[2])))
                        line_number += 1
                        if line_number == len(lines):
                            break
                        else:
                            l = lines[line_number].replace('\n', '')
                    new_seeds = []
                    for s in seeds:
                        new_seeds += maps.get_seed_ranges(s)
                    seeds = new_seeds
            line_number += 1
        min_loc = -1
        for s in seeds:
            if min_loc == -1:
                min_loc = s.range_start
            elif s.range_start < min_loc:
                min_loc = s.range_start
        print(str(min_loc))
