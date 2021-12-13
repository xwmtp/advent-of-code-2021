# https://adventofcode.com/2021/day/13
from Dict_Grid_2D import DictGrid2D

with open('input13.txt', 'r') as file:
    input = file.read()

dots_string = input.split('\n\n')[0]
folds_string = input.split('\n\n')[1]


def parse_dot_string(dot_string):
    split_string = dot_string.split(',')
    return int(split_string[0]), int(split_string[1])


def parse_folds_string(fold_string):
    split_string = fold_string[11:].split('=')
    return split_string[0], int(split_string[1])


dots = [parse_dot_string(dots_line) for dots_line in dots_string.splitlines()]
folds = [parse_folds_string(folds_line) for folds_line in folds_string.splitlines()]


# --- Part 1 --- #

def fold(grid, axis, position):
    old_grid = grid.copy()
    for y in old_grid.grid:
        for x in old_grid.grid[y]:
            if axis == 'y' and y > position:
                new_y = 2 * position - y
                grid.set(x, new_y, '#')
                grid.remove(x, y)
            if axis == 'x' and x > position:
                new_x = 2 * position - x
                grid.set(new_x, y, '#')
                grid.remove(x, y)


dot_grid = DictGrid2D()
for dot_x, dot_y in dots:
    dot_grid.set(dot_x, dot_y, '#')

first_axis, first_fold_position = folds[0]
fold(dot_grid, first_axis, first_fold_position)
print(dot_grid.count_occurrence('#'))


# --- Part 2 --- #

for fold_axis, fold_position in folds[1:]:
    fold(dot_grid, fold_axis, fold_position)
print(dot_grid)
