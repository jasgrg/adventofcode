import hashlib


def go():
    input = 'ckczppom'
    counter = 0
    while not hashlib.md5((input + str(counter)).encode()).hexdigest().startswith('000000'):
        counter += 1
    print(str(counter))
