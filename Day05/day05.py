# https://adventofcode.com/2021/day/5
from dataclasses import dataclass
from Dict_Grid_2D import Dict_Grid_2D

with open('input05.txt', 'r') as file:
    inputs = file.read().splitlines()


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:

    def __init__(self, start_point, end_point):
        self.start = start_point
        self.end = end_point
        self.is_horizontal = self.start.y == self.end.y
        self.is_vertical = self.start.x == self.end.x
        self.is_hor_vert = self.is_horizontal or self.is_vertical
        self.is_diagonal = not self.is_hor_vert
        self.x_min = min(self.start.x, self.end.x)
        self.x_max = max(self.start.x, self.end.x)
        self.y_min = min(self.start.y, self.end.y)
        self.y_max = max(self.start.y, self.end.y)


    def includes_point(self, point):
        if not self.is_hor_vert:
            return False
        return point.x >= self.start.x and point.x <= self.end.x and point.y >= self.start.y and point.y <= self.end.y

    def __str__(self):
        return f"{self.start.x},{self.start.y}->{self.end.x},{self.end.y}"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def to_line(line_string):
    point_strings = line_string.split(' -> ')
    return Line(to_point(point_strings[0]), to_point(point_strings[1]))


def to_point(point_string):
    coords = point_string.split(',')
    return Point(int(coords[0]), int(coords[1]))


lines = [to_line(inp) for inp in inputs]


# --- Part 1 --- #

hor_vert_lines = [line for line in lines if line.is_hor_vert]

def handle_vertical_line(grid, line):
    new_line_overlaps = 0
    x = line.start.x
    for y in range(line.y_min, line.y_max + 1):
        point_overlaps = add_point(grid, x, y)
        if point_overlaps == 2:
            new_line_overlaps += 1
    return new_line_overlaps

def handle_horizontal_line(grid, line):
    new_line_overlaps = 0
    y = line.start.y
    for x in range(line.x_min, line.x_max + 1):
        point_overlaps = add_point(grid, x, y)
        if point_overlaps == 2:
            new_line_overlaps += 1
    return new_line_overlaps


def add_point(grid, x, y):
    current_overlap = grid.get(x, y)
    if current_overlap is not None:
        new_overlap = current_overlap + 1
    else:
        new_overlap = 1
    grid.set(x, y, new_overlap)
    return new_overlap


overlap_count = 0
grid = Dict_Grid_2D()
for line in hor_vert_lines:
    if line.is_vertical:
        overlap_count += handle_vertical_line(grid, line)
    if line.is_horizontal:
        overlap_count += handle_horizontal_line(grid, line)
print(overlap_count)


# --- Part 2 --- #

def handle_diagonal_line(grid, line):
    x = line.start.x
    y = line.start.y
    new_line_overlaps = 0
    while (True):
        point_overlaps = add_point(grid, x, y)
        if point_overlaps == 2:
            new_line_overlaps += 1
        if line.start.x <= line.end.x:
            x += 1
        else:
            x -= 1
        if line.start.y <= line.end.y:
            y += 1
        else:
            y -= 1
        if Point(x, y) == line.end:
            return new_line_overlaps


overlap_count = 0
grid = Dict_Grid_2D()
for line in lines:
    if line.is_vertical:
        overlap_count += handle_vertical_line(grid, line)
    if line.is_horizontal:
        overlap_count += handle_horizontal_line(grid, line)
    if line.is_diagonal:
        overlap_count += handle_diagonal_line(grid, line)
print(overlap_count)
