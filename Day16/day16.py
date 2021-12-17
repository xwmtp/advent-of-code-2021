# https://adventofcode.com/2021/day/16

with open('input16.txt', 'r') as file:
    hex_input = file.read()

hexToBinary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

all_bits = ''.join(hexToBinary[hex] for hex in hex_input)


# --- Part 1 --- #

class BitsReader:

    def __init__(self, bit_string):
        self.bits = bit_string
        self.index = 0
        self.bits_countdowns = []
        self.seen_versions = []

    def read_packet(self):
        version = self.next_dec(3)
        type_id = self.next_dec(3)
        self.seen_versions.append(version)
        if type_id == 4:
            value = self.read_literal()
        else:
            value = self.read_operator(type_id)
        return value

    def read_literal(self):
        literal = ''
        while True:
            prefix = self.next_dec(1)
            literal += self.read_bits(4)
            if prefix == 0:
                return dec(literal)

    def read_operator(self, type_id):
        length_type_id = self.next_dec(1)
        if length_type_id == 0:
            values = self.read_operator_bits_count_mode()
        else:
            values = self.read_operator_packet_count_mode()
        return evaluate(values, type_id)

    def read_operator_bits_count_mode(self):
        bits_countdown = self.next_dec(15)
        self.bits_countdowns.append(bits_countdown)
        values = []
        while self.bits_countdowns[-1] != 0:
            values.append(self.read_packet())
        self.bits_countdowns.pop()
        return values

    def read_operator_packet_count_mode(self):
        packet_count = self.next_dec(11)
        values = []
        while packet_count != 0:
            values.append(self.read_packet())
            packet_count -= 1
        return values

    def read_bits(self, n):
        bits = self.bits[self.index:self.index + n]
        self.index += n
        self.countdown_bits(n)
        return bits

    def next_dec(self, n):
        return dec(self.read_bits(n))

    def countdown_bits(self, n):
        self.bits_countdowns = [count - n for count in self.bits_countdowns]


def evaluate(values, type_id):
    if type_id == 0:
        return sum(values)
    if type_id == 1:
        return product(values)
    if type_id == 2:
        return min(values)
    if type_id == 3:
        return max(values)
    if type_id == 5:
        return int(values[0] > values[1])
    if type_id == 6:
        return int(values[0] < values[1])
    if type_id == 7:
        return int(values[0] == values[1])


def dec(bits):
    return int(bits, 2)


def product(xs):
    prod = 1
    for x in xs:
        prod *= x
    return prod


bitsReader = BitsReader(all_bits)
message = bitsReader.read_packet()
print(sum(bitsReader.seen_versions))

# --- Part 2 --- #

print(message)
