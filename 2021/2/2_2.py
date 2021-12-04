from shared.helpers import read_input
from pydantic import BaseModel
from dataclasses import dataclass
from enum import Enum


class Direction(str, Enum):
    up = 'up'
    down = 'down'
    forward = 'forward'

class Command(BaseModel):
    direction: Direction
    units: int

@dataclass
class Sub:
    hpos: int = 0
    depth: int = 0
    aim: int = 0
    
    def apply(self, command: Command):
        if command.direction == Direction.up:
            self.aim = self.aim - command.units
        elif command.direction == Direction.down:
            self.aim = self.aim + command.units
        elif command.direction == Direction.forward:
            self.hpos = self.hpos + command.units
            self.depth = self.depth + (self.aim * command.units)

def line_to_cmd(line) -> Command:
    direction, units = line.split()
    return Command(direction=direction, units=units)

input = read_input(__file__)
sub = Sub()
commands = map(line_to_cmd, input)
for command in commands:
    sub.apply(command)
print(sub)
print(sub.hpos * sub.depth)


