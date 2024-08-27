from utlities import factors


def go():
    target = 36000000
    house_number = 1

    while True:
        presents = 10 * sum([i for i in factors(house_number)])
        if presents >= target:
            print(f"house number {house_number} gets {presents}")
            break
        house_number += 1
