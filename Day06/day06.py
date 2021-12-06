# https://adventofcode.com/2021/day/6
with open('input06.txt', 'r') as file:
    lines = file.read()
all_fish = [int(line) for line in lines.split(',')]


# --- Part 1 --- #

def do_naive_step(fish_array):
    for i in range(len(fish_array)):
        fish = fish_array[i]
        if fish > 0:
            fish_array[i] -= 1
        else:
            fish_array[i] = 6
            fish_array.append(8)


def simulate_naive(fish_array, times):
    fish_array_copy = fish_array.copy()
    for j in range(times):
        do_naive_step(fish_array_copy)
    return fish_array_copy


simulated_all_fish = simulate_naive(all_fish, 80)
print(len(simulated_all_fish))


# --- Part 2 --- #

def do_step(fish_dict):
    new_fish_dict = dict()
    for i in [0, 1, 2, 3, 4, 5, 7]:
        new_fish_dict[i] = fish_dict[i + 1]
    new_fish_dict[8] = fish_dict[0]
    new_fish_dict[6] = fish_dict[0] + fish_dict[7]
    return new_fish_dict


def simulate(initial_fish_dict, times):
    fish_dict = initial_fish_dict.copy()
    for j in range(times):
        fish_dict = do_step(fish_dict)
    return fish_dict


all_fish_dict = {i: 0 for i in range(9)}
for fish in all_fish:
    all_fish_dict[fish] += 1

simulated_all_fish = simulate(all_fish_dict, 256)
print(sum(simulated_all_fish.values()))
