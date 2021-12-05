# https://adventofcode.com/2021/day/4

with open('input04.txt', 'r') as file:
    lines = file.read().splitlines()
with open('input04.txt', 'r') as file:
    input_string = file.read()

numbers = [int(line) for line in lines[0].split(',')]
board_strings = input_string.split('\n\n')[1:]

# --- Part 1 --- #

class Board:

    def __init__(self, rows):
        self.rows = rows
        self.already_won = False

    def wins(self, nums):
        if self.already_won:
            return False
        wins = self.any_row_wins(nums) or self.any_col_wins(nums)
        if wins:
            self.already_won = True
            return True
        return False

    def any_row_wins(self, nums):
        for row in self.rows:
            if all(r in nums for r in row):
                return True
        return False

    def any_col_wins(self, nums):
        row_length = len(self.rows[0])
        for i in range(row_length):
            col = [row[i] for row in self.rows]
            if all(c in nums for c in col):
                return True
        return False

    def sum_unmarked(self, nums):
        sum_unmarked = 0
        for row in self.rows:
            for r in row:
                if r not in nums:
                    sum_unmarked += r
        return sum_unmarked

    def __str__(self):
        return '\n'.join([' '.join([str(r) for r in row]) for row in self.rows])


def to_board(board_string):
    rows = board_string.split('\n')
    rows = [[int(r) for r in row_str.split()] for row_str in rows]
    return Board(rows)

boards = [to_board(board_str) for board_str in board_strings]


def first_winning_board_score(boards, numbers):
    for i in range(len(numbers)):
        current_numbers = numbers[:i]
        for board in boards:
            if board.wins(current_numbers):
                return board.sum_unmarked(current_numbers) * current_numbers[-1]

print(first_winning_board_score(boards, numbers))


# --- Part 2 --- #

def find_last_winning_board_score(boards, numbers):
    last_winner_board = None
    last_winner_numbers = None
    for i in range(len(numbers)):
        current_numbers = numbers[:i]
        for board in boards:
            if board.wins(current_numbers):
                last_winner_board = board
                last_winner_numbers = current_numbers
    return last_winner_board.sum_unmarked(last_winner_numbers) * last_winner_numbers[-1]

print(find_last_winning_board_score(boards, numbers))
