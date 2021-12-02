# https://adventofcode.com/2021/day/2

with open('input02.txt', 'r') as file:
    lines = file.read().splitlines()

instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in lines]

# --- Part 1 --- #

depth = 0
horizontal = 0

for instr, amount in instructions:
    if instr == 'forward':
        horizontal += amount
    if instr == 'down':
        depth += amount
    if instr == 'up':
        depth -= amount

print(horizontal * depth)

# --- Part 2 --- #

depth = 0
horizontal = 0
aim = 0

for instr, amount in instructions:
    if instr == 'forward':
        horizontal += amount
        depth += aim * amount
    if instr == 'down':
        aim += amount
    if instr == 'up':
        aim -= amount

print(horizontal * depth)
