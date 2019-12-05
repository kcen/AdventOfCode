import re

start, end = map(int, open("./input").read().split("-"))

repeats = re.compile(r"([0-9])\1")

def valid(num):
    stringy = str(num)
    return repeats.findall(stringy) and list(stringy) == sorted(stringy)


print(sum(1 for _ in filter(valid, range(start, end))))
