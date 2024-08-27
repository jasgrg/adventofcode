from file_helpers import read_all_text


def go():
    context = read_all_text("assets/12.txt")
    total = process(eval(context))
    print(total)


def process(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, list):
        return sum([process(x) for x in obj])
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum([process(x) for x in obj.values()])
    return 0
