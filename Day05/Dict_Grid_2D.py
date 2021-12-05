class Dict_Grid_2D:

    def __init__(self):
        self.grid = dict()

    # def size(self):
    #     if len(self.grid) > 0:
    #         return (len(self.grid), len(self.grid[0]))
    #     else:
    #         return (0, 0)

    def get(self, x, y):
        if y in self.grid:
            if x in self.grid[y]:
                return self.grid[y][x]

    def set(self, x, y, to):
        if not y in self.grid:
            self.grid[y] = dict()
        self.grid[y][x] = to

    def print_points(self):
        for y, xs in self.grid.items():
            for x, value in xs.items():
                print(f"{x},{y}: {value}")

    # def count_occurence(self, target):
    #     occurrences = 0
    #     for row in self.grid:
    #         for char in row:
    #             if char == target:
    #                 occurrences += 1
    #     return occurrences

    # def __str__(self):
    #     return '\n'.join([''.join(row) for row in self.grid])

    # def copy(self):
    #     return Grid([row.copy() for row in self.grid])