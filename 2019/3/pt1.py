#!/usr/bin/env python

from dataclasses import dataclass
from collections import defaultdict


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

    def distance(self):
        return abs(self.x) + abs(self.y)


Direction = Point
direction_map = {
    "R": Direction(x=1, y=0),
    "L": Direction(x=-1, y=0),
    "U": Direction(x=0, y=1),
    "D": Direction(x=0, y=-1),
}


points = defaultdict(set)


def walk(pathlist, walker=None):
    current = Point(0, 0)
    for path in pathlist:
        direction = direction_map[path[0]]
        distance = int(path[1:])
        for _ in range(distance):
            current.x += direction.x
            current.y += direction.y
            points[walker].add(Point(x=current.x, y=current.y))


first, second = map(lambda l: l.split(","), open("./input").read().splitlines())
walk(first, "first")
walk(second, "second")
closest = sorted(points["first"] & points["second"], key=lambda p: p.distance())[0]
print(closest.distance())
