from shared.helpers import read_input, pairwise

input = read_input(__file__)
depths = map(lambda l: int(l), input)
print(len(list(filter(lambda a: a[0] < a[1], pairwise(depths)))))