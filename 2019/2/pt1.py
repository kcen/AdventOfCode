#!/usr/bin/env python

data_map = list(map(int, open("./input").read().split(",")))

# restore
data_map[1] = 12
data_map[2] = 2


def add(a, b, dest):
    data_map[dest] = data_map[a] + data_map[b]


def mult(a, b, dest):
    data_map[dest] = data_map[a] * data_map[b]


def end(*args):
    print(data_map[0])
    exit()


opcodes = {1: add, 2: mult, 99: end}

for x in range(0, len(data_map), 4):
    op = opcodes[data_map[x]]
    data_values = data_map[x + 1 : x + 4]
    op(*data_values)
