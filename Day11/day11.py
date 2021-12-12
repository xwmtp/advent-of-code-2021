# https://adventofcode.com/2021/day/11
from Grid2D import Grid2D

with open('input11.txt', 'r') as file:
    lines = file.read().splitlines()

# --- Part 1 --- #
octo_grid = Grid2D([[int(l) for l in line] for line in lines])


class OctoSimulator:

    def __init__(self, grid):
        self.flash_count = 0
        self.grid = grid.copy()

    def step(self):
        to_flash = self.increment_all()
        while len(to_flash) > 0:
            y, x = to_flash.pop()
            new_to_flash = self.flash(y, x)
            to_flash.update(new_to_flash)

    def increment_all(self):
        to_flash = set()
        for y in range(self.grid.size()[0]):
            for x in range(self.grid.size()[1]):
                current_energy = self.grid.get(y, x)
                new_energy = current_energy + 1
                self.grid.set(y, x, new_energy)
                if new_energy > 9:
                    to_flash.add((y, x))
        return to_flash

    def flash(self, y, x):
        to_flash = set()
        self.grid.set(y, x, 0)
        self.flash_count += 1
        adjacents = self.grid.get_adjacent_coords_with_diagonals(y, x)
        for adjacent in adjacents:
            adj_y, adj_x = adjacent
            current_adj_energy = self.grid.get(adj_y, adj_x)
            if current_adj_energy > 0:
                new_adj_energy = current_adj_energy + 1
                self.grid.set(adj_y, adj_x, new_adj_energy)
                if new_adj_energy > 9:
                    to_flash.add((adj_y, adj_x))
        return to_flash

    def all_flashed(self):
        return self.grid.count_occurrence(0) == 100


# --- Part 1 --- #

simulator = OctoSimulator(octo_grid)
for i in range(100):
    simulator.step()
    if simulator.all_flashed():
        break
print(simulator.flash_count)

simulator = OctoSimulator(octo_grid)
step_count = 0
while True:
    step_count += 1
    simulator.step()
    if simulator.all_flashed():
        break
print(step_count)
