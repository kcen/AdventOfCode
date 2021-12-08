from __future__ import annotations
from shared.helpers import read_input
from typing import List


input = [int(x) for x in read_input(__file__)[0].split(',')]

def distance(n):
    return sum(triangular(abs(x - n)) for x in input)

def triangular(n):
    return int((n * (n + 1))/2)

print(min(distance(i) for i in range(max(input))))