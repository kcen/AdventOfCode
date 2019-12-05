#!/usr/bin/env python

from itertools import product
from copy import copy

initial_input = list(map(int, open("./input").read().split(",")))
data_map = None


class ExecutionFinish(StopIteration):
    ...


def reset(noun=12, verb=2):
    global data_map
    data_map = copy(initial_input)
    data_map[1] = noun
    data_map[2] = verb


def add(a, b, dest):
    data_map[dest] = data_map[a] + data_map[b]


def mult(a, b, dest):
    data_map[dest] = data_map[a] * data_map[b]


def end(*args):
    raise ExecutionFinish()


opcodes = {1: add, 2: mult, 99: end}


def run(noun, verb):
    global data_map
    reset(noun, verb)
    try:
        for x in range(0, len(data_map), 4):
            op = opcodes[data_map[x]]
            data_values = data_map[x + 1 : x + 4]
            op(*data_values)
    except ExecutionFinish:
        pass
    return data_map[0]


for noun, verb in product(range(0, 100), range(0, 100)):
    result = run(noun, verb)
    if result == 19690720:
        print(f"{noun},{verb}, {result}")
        print(100 * noun + verb)
        exit()
