# https://adventofcode.com/2021/day/10
import math

with open('input10.txt', 'r') as file:
    lines = file.read().splitlines()


# --- Part 1 --- #

BRACKET_PAIRS = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

OPENING_BRACKETS = list(BRACKET_PAIRS.keys())
CLOSING_BRACKETS = list(BRACKET_PAIRS.values())

SCORE_TABLE_CORRUPTED_LINE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def syntax_score_line(line):
    stack = []
    for bracket in line:
        if bracket in OPENING_BRACKETS:
            stack.append(BRACKET_PAIRS[bracket])
        else:
            popped = stack.pop()
            if popped != bracket:
                return SCORE_TABLE_CORRUPTED_LINE[bracket]
    return 0


incomplete_lines = []
syntax_error_score = 0
for line in lines:
    score = syntax_score_line(line)
    syntax_error_score += syntax_score_line(line)
    if score == 0:
        incomplete_lines.append(line)
print(syntax_error_score)


# --- Part 2 --- #

SCORE_TABLE_INCOMPLETE_LINE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def autocomplete_score_line(line):
    stack = []
    for bracket in line:
        if bracket in OPENING_BRACKETS:
            stack.append(BRACKET_PAIRS[bracket])
        else:
            popped = stack.pop()
            if popped != bracket:
                raise Exception('corrupted!')
    return calculate_score(reversed(stack))


def calculate_score(brackets):
    total_score = 0
    for bracket in brackets:
        total_score *= 5
        total_score += SCORE_TABLE_INCOMPLETE_LINE[bracket]
    return total_score


autocomplete_scores = [autocomplete_score_line(line) for line in incomplete_lines]
print(sorted(autocomplete_scores)[math.floor(len(autocomplete_scores) / 2)])
