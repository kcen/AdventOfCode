from shared.helpers import read_input
from collections import deque
from numpy import matrix, vectorize

input = read_input(__file__)
num_boards = int((len(input) - 1) / 6)

# Parse input
consumeable = deque(input)
draw_numbers = [int(i) for i in consumeable.popleft().split(',')]
_ = consumeable.popleft()
boards = []
for i in range(num_boards):
    board = ' ; '.join([consumeable.popleft() for _ in range(5)])
    if i + 1 != num_boards:
        _ = consumeable.popleft()
    boards.append(matrix(board))

chosen_numbers = set()
selected = vectorize(lambda v: 1 if v in chosen_numbers else 0)

# Check win condition
def bingo_losers(boards):
    losers = []
    for board in boards:
        rows = selected(board).tolist()
        columns = selected(board.transpose()).tolist()
        winner = list(all(x) for x in rows + columns)
        if not any(winner):
            losers.append(board)
    return losers

losing_board = None
winning_num = None

for draw_num in draw_numbers:
    winning_num = draw_num
    chosen_numbers.add(draw_num)
    losers = bingo_losers(boards)
    if len(losers) == 1:
        losing_board = losers[0]
    elif len(losers) == 0:
        break

unchosen_nums = [x for x in losing_board.ravel().tolist()[0] if x not in chosen_numbers]
sum_unchosen = sum(unchosen_nums)
print(f"{sum_unchosen} * {winning_num} = {sum_unchosen * winning_num}")