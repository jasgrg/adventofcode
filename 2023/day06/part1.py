from file_helpers import open_file, get_next_line


def go():
    open_file("assets/6_races.txt")
    line_number, l, eof = get_next_line()
    times = [int(t) for t in l.split(' ')[1:] if t != '']
    line_number, l, eof = get_next_line()
    distances = [int(t) for t in l.split(' ')[1:] if t != '']
    total = 1
    for i in range(0, len(times)):
        t = times[i]
        d = distances[i]
        winning_count = 0
        for hold in range(0, t):
            distance_traveled = (hold) * (t - hold)
            if distance_traveled > d:
                winning_count += 1
        total *= winning_count

    print(str(total))
