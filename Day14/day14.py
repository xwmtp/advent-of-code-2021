# https://adventofcode.com/2021/day/14
import math

with open('input14.txt', 'r') as file:
    input = file.read()

polymer_template = input.split('\n\n')[0]
insertion_strings = input.split('\n\n')[1].splitlines()
insertion_rules = {string.split(' -> ')[0]: string.split(' -> ')[1] for string in insertion_strings}


def get_all_elements(rules):
    all_elements = set()
    for left, right_element in rules.items():
        for left_element in left:
            all_elements.add(left_element)
        all_elements.add(right_element)
    return all_elements


def get_initial_pairs_count(template):
    pairs_count = {}
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        if pair not in pairs_count:
            pairs_count[pair] = 0
        pairs_count[pair] += 1
    return pairs_count


def step(pairs_count):
    for pair, count in list(pairs_count.items()):
        new_pair_1 = pair[0] + insertion_rules[pair]
        new_pair_2 = insertion_rules[pair] + pair[1]

        add_count(new_pair_1, pairs_count, count)
        add_count(new_pair_2, pairs_count, count)
        pairs_count[pair] -= count
        if pairs_count[pair] == 0:
            del pairs_count[pair]


def add_count(key, dct, count):
    if key not in dct:
        dct[key] = count
    else:
        dct[key] += count


def count_occurrence(pairs_count, element):
    count = 0
    for pair, pair_count in pairs_count.items():
        count += pair_count * pair.count(element)
    return math.ceil(count / 2)


def element_occurrences(pairs_count):
    return {element: count_occurrence(pairs_count, element) for element in ALL_ELEMENTS}


ALL_ELEMENTS = get_all_elements(insertion_rules)
pairs_count_dict = get_initial_pairs_count(polymer_template)

# --- Part 1 --- #
for i in range(10):
    step(pairs_count_dict)
    elements = element_occurrences(pairs_count_dict)
print(max(elements.values()) - min(elements.values()))

for i in range(30):
    step(pairs_count_dict)
    elements = element_occurrences(pairs_count_dict)
print(max(elements.values()) - min(elements.values()))
