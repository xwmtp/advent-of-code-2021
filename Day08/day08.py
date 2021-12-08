# https://adventofcode.com/2021/day/8

with open('input08.txt', 'r') as file:
    lines = file.read().splitlines()


def parse_line(line):
    signal_patterns_string = line.split(' | ')[0]
    output_values_string = line.split(' | ')[1]

    signal_patterns = signal_patterns_string.split()
    output_values = output_values_string.split()
    return {'signal': signal_patterns, 'output': output_values}


entries = [parse_line(line) for line in lines]

# --- Part 1 --- #

unique_length_segments = {
    1: ['c', 'f'],
    4: ['b', 'c', 'd', 'f'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
}

unique_lengths = {len(segments): digit for digit, segments in unique_length_segments.items()}


def unique_length_digits_occurrences(output_digits_per_entry):
    unique_length_digits_count = 0
    for output_digits in output_digits_per_entry:
        for output_digit in output_digits:
            if len(output_digit) in unique_lengths:
                unique_length_digits_count += 1
    return unique_length_digits_count


output_digits_per_entry = [entry['output'] for entry in entries]
print(unique_length_digits_occurrences(output_digits_per_entry))


# --- Part 2 --- #

def identify_patterns(patterns):
    identified_patterns = identify_unique_length_patterns(patterns)
    identified_patterns.update(identify_len_5_patterns(patterns))
    identified_patterns.update(identify_len_6_patterns(patterns))
    return identified_patterns


def identify_unique_length_patterns(patterns):
    identified_patterns = {}
    for pattern in patterns:
        if len(pattern) in unique_lengths:
            identified_patterns[pattern] = unique_lengths[len(pattern)]
    return identified_patterns


def identify_len_5_patterns(patterns):
    identified_patterns = {}
    pattern_digit_1 = next(pattern for pattern in patterns if len(pattern) == 2)
    patterns_length_5 = [pattern for pattern in patterns if len(pattern) == 5]

    for pattern in patterns_length_5:
        if pattern_digit_1[0] in pattern and pattern_digit_1[1] in pattern:
            identified_patterns[pattern] = 3

    pattern_d4 = next(pattern for pattern in patterns if len(pattern) == 4)
    pattern_d4_without_d1 = remove_from_pattern(pattern_d4, pattern_digit_1)

    if all(pattern_d4_without_d1[0] in pattern for pattern in patterns_length_5):
        segment_b = pattern_d4_without_d1[1]
    else:
        segment_b = pattern_d4_without_d1[0]

    for pattern in patterns_length_5:
        if pattern in identified_patterns:
            continue
        if segment_b in pattern:
            identified_patterns[pattern] = 5
        else:
            identified_patterns[pattern] = 2
    return identified_patterns


def identify_len_6_patterns(patterns):
    identified_patterns = {}
    pattern_digit_1 = next(s for s in patterns if len(s) == 2)
    patterns_length_6 = [s for s in patterns if len(s) == 6]

    pattern_digit_4 = next(s for s in patterns if len(s) == 4)
    pattern_d4_without_d1 = remove_from_pattern(pattern_digit_4, pattern_digit_1)

    if all(pattern_d4_without_d1[0] in pattern for pattern in patterns_length_6):
        segment_d = pattern_d4_without_d1[1]
    else:
        segment_d = pattern_d4_without_d1[0]

    for pattern in patterns_length_6:
        if segment_d not in pattern:
            identified_patterns[pattern] = 0

    for pattern in patterns_length_6:
        if pattern in identified_patterns:
            continue
        if pattern_digit_1[0] in pattern and pattern_digit_1[1] in pattern:
            identified_patterns[pattern] = 9
        else:
            identified_patterns[pattern] = 6
    return identified_patterns


def remove_from_pattern(pattern, letters):
    for letter in letters:
        pattern = pattern.replace(letter, '')
    return pattern


def decode(entries):
    sum_decoded = 0
    for entry in entries:
        identified_patterns = identify_patterns(entry['signal'])

        decoded = ''
        for output_digit in entry['output']:
            for pattern, number in identified_patterns.items():
                if sorted(output_digit) == sorted(pattern):
                    decoded += str(number)
                    break
        sum_decoded += int(decoded)
    return sum_decoded


print(decode(entries))
