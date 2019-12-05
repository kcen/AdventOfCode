#!/usr/bin/env python

data_map = map(int, open("./input").read().splitlines())

output = sum(map(lambda x: x // 3 - 2, data_map))
print(output)
