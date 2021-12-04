from shared.helpers import read_input, triwise, pairwise

input = read_input(__file__)
depths = map(lambda l: int(l), input)
groups = triwise(depths)
sums = map(sum, groups)
print(len(list(filter(lambda a: a[0] < a[1], pairwise(sums)))))