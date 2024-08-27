deer = {}
deer['Vixen'] = {"speed": 8, "fly": 8, "rest": 53, "score": 0,
                 "dist": 0}  # can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
deer['Blitzen'] = {"speed": 13, "fly": 4,
                   "rest": 49, "score": 0,
                   "dist": 0}  # can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
deer['Rudolph'] = {"speed": 20, "fly": 7,
                   "rest": 132, "score": 0,
                   "dist": 0}  # can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
deer['Cupid'] = {"speed": 12, "fly": 4, "rest": 43, "score": 0,
                 "dist": 0}  # can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
deer['Donner'] = {"speed": 9, "fly": 5, "rest": 38, "score": 0,
                  "dist": 0}  # can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
deer['Dasher'] = {"speed": 10, "fly": 4,
                  "rest": 37, "score": 0,
                  "dist": 0}  # can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
deer['Comet'] = {"speed": 3, "fly": 37, "rest": 76, "score": 0,
                 "dist": 0}  # can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
deer['Prancer'] = {"speed": 9, "fly": 12,
                   "rest": 97, "score": 0,
                   "dist": 0}  # can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
deer['Dancer'] = {"speed": 37, "fly": 1,
                  "rest": 36, "score": 0,
                  "dist": 0}  # can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.


def go():
    seconds = 2503
    for sec in range(1, seconds + 1):
        print(f"after {sec} seconds")
        for d in deer.keys():
            cycle = deer[d]['fly'] + deer[d]['rest']
            remainder = sec % cycle
            if 0 < remainder <= deer[d]['fly']:
                deer[d]['dist'] += deer[d]['speed']
        max_dist = 0
        for d in deer.values():
            if d['dist'] > max_dist:
                max_dist = d['dist']
        for d in deer.keys():
            if deer[d]['dist'] == max_dist:
                deer[d]['score'] += 1
            print(f"{d} : {deer[d]['dist']} - {deer[d]['score']}")
    max_score = 0
    for d in deer.values():
        if d['score'] == max_score:
            max_score = d['score']
    print(max_score)
