from shared.helpers import read_input, boollist2int
from collections import defaultdict

input = read_input(__file__)
bit_input = list([int(b) for b in l] for l in input)

bit_len = len(input[0])
total_lines = len(input)
counts = []
for i in range(bit_len):
    count = defaultdict(int)
    for bit_line in bit_input:
        bit = bit_line[i]
        count[bit] += 1
    counts.append(count)
        
gamma = boollist2int([c[1] > c[0] for c in counts])
epsilon =  boollist2int([c[1] < c[0] for c in counts])
print(gamma)
print(epsilon)
print(gamma * epsilon)