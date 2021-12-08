from __future__ import annotations
from shared.helpers import read_input
from pydantic import BaseModel
import re
from typing import List


input = [int(x) for x in read_input(__file__)[0].split(',')]
count_days_remain: List[int] = [input.count(x) for x in range(9)]

def advance():
    new_fish = count_days_remain[0]
    old_fish = count_days_remain[1:]
    old_fish.extend([0] * (9 - len(old_fish)))
    old_fish[6] += new_fish
    old_fish[8] = new_fish
    return old_fish

for _ in range(256):
    count_days_remain = advance()
print(sum(count_days_remain))