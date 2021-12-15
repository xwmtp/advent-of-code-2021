# https://adventofcode.com/2021/day/15
from Grid2D import Grid2D
from A_Star import A_star

with open('input15.txt', 'r') as file:
    row_strings = file.read().splitlines()

risk_rows = [[int(r) for r in row] for row in row_strings]


# --- Part 1 --- #

class Maze:

    def __init__(self, grid):
        self.grid = grid
        self.start = 0, 0
        x_size, y_size = grid.size()
        self.end = x_size - 1, y_size - 1

    def adjacents(self, state):
        x, y = state
        return self.grid.get_adjacent_coords(x, y)

    def neighbour_cost(self, state1, state2):
        x2, y2 = state2
        return self.grid.get(x2, y2)

    def heuristic(self, state1, state2):
        return 0


a_star = A_star()
maze = Maze(Grid2D(risk_rows))
shortest_path = a_star.search(maze.start, maze.end, maze)
risks = [maze.grid.get(x, y) for x, y in shortest_path]
print(sum(risks) - maze.grid.get(0, 0))


# --- Part 2 --- #

def get_x5_width(rows):
    increased_rows = []
    for row in rows:
        new_row = row.copy()
        prev_row = new_row
        for _ in range(4):
            increased = increased_row(prev_row)
            new_row += increased
            prev_row = increased
        increased_rows.append(new_row)
    return increased_rows


def get_x5_height(rows):
    total_new_rows = [row.copy() for row in rows]
    prev_rows = [row.copy() for row in rows]
    for _ in range(4):
        added_rows = []
        for row in prev_rows:
            new_row = increased_row(row)
            total_new_rows.append(new_row)
            added_rows.append(new_row)
        prev_rows = added_rows
    return total_new_rows


def increased_row(row):
    return [max(1, (num + 1) % 10) for num in row]


a_star_5x5 = A_star()
rows_x5_width = get_x5_width(risk_rows)
rows_5x5 = get_x5_height(rows_x5_width)
maze_5x5 = Maze(Grid2D(rows_5x5))

shortest_path = a_star_5x5.search(maze_5x5.start, maze_5x5.end, maze_5x5)
risks = [maze_5x5.grid.get(x, y) for x, y in shortest_path]
print(sum(risks) - maze.grid.get(0, 0))
