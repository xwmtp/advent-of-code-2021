# https://adventofcode.com/2021/day/7
import sys

with open('input07.txt', 'r') as file:
    lines = file.read()
positions = [int(line) for line in lines.split(',')]

max_pos = max(positions)
min_pos = min(positions)

# --- Part 1 --- #

min_total_fuel = sys.maxsize
for i in range(min_pos, max_pos + 1):
    total_fuel = 0
    for pos in positions:
        total_fuel += abs(pos - i)
    if total_fuel < min_total_fuel:
        min_total_fuel = total_fuel

print(min_total_fuel)


# --- Part 2 --- #

def triangular_number(n):
    return int((n * (n + 1)) / 2)


min_total_fuel = sys.maxsize
for i in range(min_pos, max_pos + 1):
    total_fuel = 0
    for pos in positions:
        total_fuel += triangular_number(abs(pos - i))
    if total_fuel < min_total_fuel:
        min_total_fuel = total_fuel

print(min_total_fuel)
