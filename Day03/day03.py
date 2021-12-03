# https://adventofcode.com/2021/day/3

with open('input03.txt', 'r') as file:
    diagnostic_bins = file.read().splitlines()

# --- Part 1 --- #

epsilon_bin = ''
gamma_bin = ''
for i in range(len(diagnostic_bins[0])):
    bit_sum = sum([int(b[i]) for b in diagnostic_bins])
    if bit_sum > (len(diagnostic_bins) / 2):
        epsilon_bin += '1'
        gamma_bin += '0'
    else:
        epsilon_bin += '0'
        gamma_bin += '1'

epsilon_rate = int(epsilon_bin, 2)
gamma_rate = int(gamma_bin, 2)
power_consumption = epsilon_rate * gamma_rate
print(power_consumption)


# --- Part 2 --- #

def calculate_rating(rating_type='oxygen'):
    remaining_bins = diagnostic_bins
    for i in range(len(remaining_bins[0])):
        if len(remaining_bins) == 1:
            break
        total = sum([int(remaining_bin[i]) for remaining_bin in remaining_bins])
        if total >= (len(remaining_bins) / 2):
            bit_criteria = '1' if rating_type == 'oxygen' else '0'
        else:
            bit_criteria = '0' if rating_type == 'oxygen' else '1'
        remaining_bins = [b for b in remaining_bins if b[i] == bit_criteria]
    return int(remaining_bins[0], 2)


oxygen_rating = calculate_rating('oxygen')
co2_rating = calculate_rating('co2')
life_support_rating = oxygen_rating * co2_rating
print(life_support_rating)
