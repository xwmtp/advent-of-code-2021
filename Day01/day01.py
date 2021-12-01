# https://adventofcode.com/2021/day/1
import sys

with open('input01.txt', 'r') as file:
    raw_depths = file.read().splitlines()
depths = [int(depth) for depth in raw_depths]


# --- Part 1 --- #
number_increases = 0
prev_depth = sys.maxsize
for depth in depths:
    if depth > prev_depth:
        number_increases += 1
    prev_depth = depth
print(number_increases)


# --- Part 2 --- #
window_increases = 0
prev_window = sys.maxsize
for i in range(len(depths) - 2):
    window = sum(depths[i:i+3])
    if window > prev_window:
        window_increases += 1
    prev_window = window
print(window_increases)
