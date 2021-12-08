from __future__ import annotations
from shared.helpers import read_input
from typing import List


input = [int(x) for x in read_input(__file__)[0].split(',')]

def distance(n):
    return sum(abs(x - n) for x in input)

print(min(distance(i) for i in range(max(input))))