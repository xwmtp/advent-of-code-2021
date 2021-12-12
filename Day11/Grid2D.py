class Grid2D:

    def __init__(self, rows):
        self.grid = rows

    def size(self):
        if len(self.grid) > 0:
            return len(self.grid), len(self.grid[0])
        else:
            return 0, 0

    def get(self, y, x):
        return self.grid[y][x]

    def set(self, y, x, to):
        self.grid[y][x] = to

    def count_occurrence(self, target):
        occurrences = 0
        for row in self.grid:
            for char in row:
                if char == target:
                    occurrences += 1
        return occurrences

    def get_adjacent_coords(self, y, x):
        adjacents = []
        for diff in [-1, 1]:
            adj_y = y + diff
            adj_x = x + diff
            if 0 <= adj_y < self.size()[0]:
                adjacents.append((adj_y, x))
            if 0 <= adj_x < self.size()[1]:
                adjacents.append((y, adj_x))
        if (y, x) in adjacents:
            adjacents.remove((y, x))
        return adjacents

    def get_adjacent_coords_with_diagonals(self, y, x):
        adjacents = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                adj_y = y + dy
                adj_x = x + dx
                if 0 <= adj_y < self.size()[0] and 0 <= adj_x < self.size()[0]:
                    adjacents.append((adj_y, adj_x))
        if (y, x) in adjacents:
            adjacents.remove((y, x))
        return adjacents


    def get_adjecent_values(self, y, x):
        coords = self.get_adjacent_coords(y, x)
        return [self.get(y, x) for y, x in coords]

    def __str__(self):
        return '\n'.join([''.join(str(r) for r in row) for row in self.grid])

    def copy(self):
        return Grid2D([row.copy() for row in self.grid])
