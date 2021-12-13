class DictGrid2D:

    def __init__(self):
        self.grid = dict()

    def size(self):
        max_x = 0
        max_y = 0
        for y in self.grid:
            if y > max_y:
                max_y = y
            for x in self.grid[y]:
                if x > max_x:
                    max_x = x
        return max_x, max_y

    def get(self, x, y):
        if y in self.grid:
            if x in self.grid[y]:
                return self.grid[y][x]

    def set(self, x, y, to):
        if y not in self.grid:
            self.grid[y] = dict()
        self.grid[y][x] = to

    def remove(self, x, y):
        if y in self.grid:
            if x in self.grid[y]:
                del self.grid[y][x]
            if len(self.grid[y]) == 0:
                del self.grid[y]

    def print_points(self):
        for y, xs in self.grid.items():
            for x, value in xs.items():
                print(f"{x},{y}: {value}")

    def count_occurrence(self, target):
        count = 0
        for xs in self.grid.values():
            for value in xs.values():
                if value == target:
                    count += 1
        return count

    def __str__(self):
        rows = []
        for y in range(self.size()[1] + 1):
            row = ''
            for x in range(self.size()[0] + 1):
                value = self.get(x, y)
                if not value:
                    row += '_'
                else:
                    row += value
            rows.append(row)
        return '\n'.join(rows)

    def copy(self):
        new_grid = DictGrid2D()
        for y in self.grid:
            for x in self.grid[y]:
                new_grid.set(x, y, self.grid[y][x])
        return new_grid
