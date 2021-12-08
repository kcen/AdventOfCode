from __future__ import annotations
from shared.helpers import read_input
from pydantic import BaseModel
import re
from typing import List
from numpy import array, zeros


input = read_input(__file__)
POND: List[LanternFish] = []

def make_lantern(string: i = '8'):
    return LanternFish(days_until=i)

class LanternFish(BaseModel):
    days_until: int

    def advance(self):
        if self.days_until == 0:
            self.birth()
            self.days_until = 6
        else:
            self.days_until -= 1
    def birth(self):
        POND.append(LanternFish(days_until=8))

for i in input[0].split(','):
    POND.append(make_lantern(i))

def p():
    return ','.join(str(f.days_until) for f in POND)

day = 0
while day < 15:
    #print(f"DAY: {day} POND: {p()}")
    print(len(POND))
    for fish in list(POND):
        minnow = fish.advance()
    day += 1

print(len(POND))