start, end = map(int, open("input").read().split("-"))
ordered = lambda s: list(s) == sorted(s)
paired = lambda s: any(s.count(c) == 2 for c in set(s))
valid = lambda s: ordered(s) and paired(s)
print(sum(1 for _ in filter(valid, map(str, range(start, end)))))
