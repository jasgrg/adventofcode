import hashlib


def part1():
    base = "uqwqemis"

    index = 0
    password = ''

    while True:
        md5_hash = hashlib.md5()
        md5_hash.update(f"{base}{index}".encode('utf-8'))
        hash = md5_hash.hexdigest()
        if hash.startswith("00000"):
            password += hash[5]
            if len(password) == 8:
                print(f"{index} - {password}")
                exit(0)
        index += 1


def part2():
    base = "uqwqemis"

    index = 0
    password = '________'

    while True:
        md5_hash = hashlib.md5()
        md5_hash.update(f"{base}{index}".encode('utf-8'))
        hash = md5_hash.hexdigest()
        if hash.startswith("00000"):
            pos = int(hash[5], 16)
            if pos < 8 and password[pos] == '_':
                password = password[:pos] + hash[6] + password[pos + 1:]
                if '_' not in password:
                    print(f"{index} - {password}")
                    exit(0)
        index += 1


part2()
