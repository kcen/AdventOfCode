#!/usr/bin/env python

data_map = map(int, open("./input").read().splitlines())


def module_fuel(weight):
    fuel_req = weight // 3 - 2
    if fuel_req < 0:
        return 0
    if fuel_req >= 9:
        fuel_req += module_fuel(fuel_req)
    return fuel_req


output = sum(map(module_fuel, data_map))
print(output)
