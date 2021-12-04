from pathlib import Path
from typing import List
from itertools import tee

def read_input(relative_file) -> List[str]:
    path = Path(relative_file).parent / "input"
    with path.open() as f:
        return [line for line in f]

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