from __future__ import annotations
from shared.helpers import read_input
from pydantic import BaseModel
import re
from typing import List
from numpy import array, zeros


input = read_input(__file__)
LINE_PATTERN = re.compile("(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)")

class Line(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int

    def parse(input_line) -> Line:
        fields = LINE_PATTERN.match(input_line).groupdict()
        return Line.parse_obj(fields)

    def vert_horiz(self) -> bool:
        return (self.x1 == self.x2) or (self.y1 == self.y2)
    
    def max_val(self) -> int:
        return max([self.max_x(), self.max_y()])
    
    def max_x(self) -> int:
        return max([self.x1, self.x2])

    def max_y(self) -> int:
        return max([self.y1, self.y2])


lines: List[Line] = [Line.parse(l) for l in input]
horiz_vert: List[Line] = [l for l in lines if l.vert_horiz()]

max_x = max(l.max_x() for l in horiz_vert)
max_y = max(l.max_y() for l in horiz_vert)

# We need 1 extra row to handle zero index
board = zeros((max_y + 1, max_x + 1), dtype=int)

for line in lines:
    if line.x1 == line.x2:
        x = line.x1
        y_range = [line.y1, line.y2]
        for y in range(min(y_range), max(y_range) + 1):
            board[y,x] += 1

    if line.y1 == line.y2:
        y = line.y1
        x_range = [line.x1, line.x2]
        for x in range(min(x_range), max(x_range) + 1):
            board[y,x] += 1

print(len([p for p in board.flatten() if p >=2]))
