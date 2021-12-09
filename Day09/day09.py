# https://adventofcode.com/2021/day/9
from Grid2D import Grid2D

with open('input09.txt', 'r') as file:
    lines = file.read().splitlines()

grid = Grid2D([line for line in lines])


# --- Part 1 --- #

def get_low_points(grid):
    low_points = []
    grid_size = grid.size()
    for y in range(grid_size[0]):
        for x in range(grid_size[1]):
            current_height = int(grid.get(y, x))
            adj_heights = [int(h) for h in grid.get_adjecent_values(y, x)]
            if all(current_height < height for height in adj_heights):
                low_points.append((y, x))
    return low_points


low_points = get_low_points(grid)
low_point_risk_level_sum = sum(1 + int(grid.get(y, x)) for y, x in low_points)
print(low_point_risk_level_sum)


# --- Part 2 --- #

def find_basin_of_low_point(low_point):
    basin_points = set()
    y, x = low_point

    to_check = set(grid.get_adjacent_coords(y, x))
    already_checked = set()
    while len(to_check) > 0:
        y, x = to_check.pop()
        if (y, x) in already_checked:
            continue
        if grid.get(y, x) != '9':
            basin_points.add((y, x))
            to_check.update(grid.get_adjacent_coords(y, x))
        already_checked.add((y, x))
    return basin_points


def already_contains(basins, new_basin):
    for basin in basins:
        if set(basin) == new_basin:
            return True
    return False


def multiply(xs):
    product = 1
    for x in xs:
        product *= x
    return product


basins = []
for low_point in low_points:
    found_basin = find_basin_of_low_point(low_point)
    if not already_contains(basins, found_basin):
        basins.append(found_basin)

print(multiply(sorted([len(basin) for basin in basins], reverse=True)[:3]))
