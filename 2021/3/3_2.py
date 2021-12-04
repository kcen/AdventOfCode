from shared.helpers import read_input, boollist2int
from collections import defaultdict

input = read_input(__file__)
bit_input = list([int(b) for b in l] for l in input)

def bit_counts(inputs, pos):
    count = defaultdict(int)
    for i in inputs:
        bit = i[pos]
        count[bit] +=1
    return count

# Defaults 1 for tie
def max_key(d):
    val = 1 if d[1] >= d[0] else 0
    return val

# Oxygen (Most common bit)
oxygen_list = [x for x in bit_input]
pos = 0
while len(oxygen_list) > 1:
    # print(f"Checking pos:{pos}")
    #Most common
    count = bit_counts(oxygen_list, pos)
    keep = max_key(count)
    oxygen_list = [x for x in oxygen_list if x[pos] == keep]
    pos += 1
oxygen = boollist2int(oxygen_list[0])


# CO2
co2_list = [x for x in bit_input]
pos = 0
while len(co2_list) > 1:
    # print(f"Checking pos:{pos}")
    #Most common
    count = bit_counts(co2_list, pos)
    reject = max_key(count)
    co2_list = [x for x in co2_list if x[pos] != reject]
    pos += 1
co2 = boollist2int(co2_list[0])


print(f"{oxygen} * {co2} = {oxygen * co2}")