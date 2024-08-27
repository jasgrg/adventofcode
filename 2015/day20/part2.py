def go():
    target = 36000000
    house_number = 1
    while True:
        presents = 11 * sum([house_number // n for n in range(1, 51) if house_number % n == 0])
        if presents >= target:
            print(f"house number {house_number} gets {presents}")
            break

        house_number += 1
