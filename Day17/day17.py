## https://adventofcode.com/2021/day/17
from Dict_Grid_2D import DictGrid2D

with open('input17.txt', 'r') as file:
    target_area_string = file.read()

target_coords_string = target_area_string[13:]


def parse_coord(coord_string):
    numbers_string = coord_string.split('=')[1]
    numbers = [int(num) for num in numbers_string.split('..')]
    return numbers[0], numbers[1]


target_x_range = parse_coord(target_coords_string.split(', ')[0])
target_y_range = parse_coord(target_coords_string.split(', ')[1])


# --- Part 1 --- #

class Probe:

    def __init__(self, target_x_min, target_x_max, target_y_min, target_y_max):
        self.x = 0
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.target_x_min = target_x_min
        self.target_x_max = target_x_max
        self.target_y_min = target_y_min
        self.target_y_max = target_y_max
        self.shoot_grid = None
        self.y_max = 0
        self.reached_target = False

    def reset(self):
        self.x = 0
        self.y = 0
        self.shoot_grid = None
        self.reached_target = False
        self.y_max = 0

    def step(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        if self.y > self.y_max:
            self.y_max = self.y
        if self.is_in_target():
            self.reached_target = True
        if self.velocity_x != 0:
            self.velocity_x += 1 if self.velocity_x < 0 else -1
        self.velocity_y -= 1
        self.shoot_grid.set(self.x, -self.y, '#')
        # print(self)

    def shoot(self, init_velocity_x, init_velocity_y, min_y):
        self.reset()
        self.shoot_grid = DictGrid2D()
        self.velocity_x = init_velocity_x
        self.velocity_y = init_velocity_y
        while self.y > min_y:
            self.step()
        # print(self.shoot_grid)

    def is_in_target(self):
        return self.target_x_min <= self.x <= self.target_x_max and self.target_y_min <= self.y <= self.target_y_max

    def __str__(self):
        return f"({self.x}, {self.y}) vel_x: {self.velocity_x}, vel_y: {self.velocity_y}"


min_y = min(target_y_range) - 20
probe = Probe(target_x_range[0], target_x_range[1], target_y_range[0], target_y_range[1])
probe.shoot(12, 10, min(target_y_range) - 20)

reached_target_count = 0
overall_y_max = 0
for x in range(0, 170):
    for y in range(-170, 170):
        probe.shoot(x, y, min_y)
        if not probe.reached_target:
            continue
        reached_target_count += 1
        if probe.y_max > overall_y_max:
            overall_y_max = probe.y_max

print(overall_y_max)


# --- Part 2 --- #

print(reached_target_count)
