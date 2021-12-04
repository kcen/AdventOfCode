from pathlib import Path
from typing import List, Dict
from itertools import tee

def read_input(relative_file) -> List[str]:
    path = Path(relative_file).parent / "input"
    with path.open() as f:
        return [line.strip() for line in f]

def pairwise(seq):
    a, b = tee(seq)
    next(b, None)
    return zip(a, b)

def triwise(seq):
    a, b, c = tee(seq, 3)
    next(b)
    next(c)
    next(c)
    return zip(a, b, c)

def boollist2int(l: List[bool]):
    return sum(2**i for i, v in enumerate(reversed(l)) if v)
