#!/usr/bin/env python

from dataclasses import dataclass
from collections import defaultdict


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int


Direction = Point
direction_map = {
    "R": Direction(x=1, y=0),
    "L": Direction(x=-1, y=0),
    "U": Direction(x=0, y=1),
    "D": Direction(x=0, y=-1),
}


points = defaultdict(list)


def walk(pathlist, walker=None):
    current = Point(x=0, y=0)
    for path in pathlist:
        direction = direction_map[path[0]]
        distance = int(path[1:])
        for _ in range(distance):
            current.x += direction.x
            current.y += direction.y
            points[walker].append(Point(x=current.x, y=current.y))


first, second = map(lambda l: l.split(","), open("./input").read().splitlines())
walk(first, "first")
walk(second, "second")
intersections = set(points["first"]) & set(points["second"])
distance = float("inf")
for p in intersections:
    d = points["first"].index(p) + 1 + points["second"].index(p) + 1
    distance = min(distance, d)

print(distance)
