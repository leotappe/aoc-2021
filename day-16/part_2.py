"""
Advent of Code 2021 | Day 16 | Part 2
"""
import sys
import math


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

class Literal(Packet):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def sum_version_numbers(self):
        return self.version

    def eval(self):
        return self.value

    def __str__(self):
        return f'L-{self.version}-{self.type_id}({self.value})'


class Operator(Packet):
    def __init__(self, version, type_id, length_type_id):
        super().__init__(version, type_id)
        self.length_type_id = length_type_id
        self.subpackets = []

    def sum_version_numbers(self):
        return self.version + sum(packet.sum_version_numbers() for packet in self.subpackets)

    def eval(self):
        if self.type_id == 0:
            return sum(p.eval() for p in self.subpackets)
        if self.type_id == 1:
            return math.prod(p.eval() for p in self.subpackets)
        if self.type_id == 2:
            return min(p.eval() for p in self.subpackets)
        if self.type_id == 3:
            return max(p.eval() for p in self.subpackets)
        if self.type_id == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        if self.type_id == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        if self.type_id == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())
    
    def __str__(self):
        return f'O-{self.version}-{self.type_id}({",".join(str(packet) for packet in self.subpackets)})'


def get_version(bits, start_index):
    return int(bits[start_index:start_index + 3], base=2)


def get_type_id(bits, start_index):
    return int(bits[start_index + 3:start_index + 6], base=2)


def get_literal_value(bits, start_index):
    groups = []
    for i in range(start_index + 6, len(bits), 5):
        groups.append(bits[i + 1:i + 5])
        if bits[i] == '0':
            break
    return int(''.join(groups), base=2), i + 5


def get_length_type_id(bits, start_index):
    return int(bits[start_index + 6])


def get_total_length_of_subpackets_in_bits(bits, start_index):
    return int(bits[start_index + 7:start_index + 7 + 15], base=2)


def get_number_of_subpackets(bits, start_index):
    return int(bits[start_index + 7:start_index + 7 + 11], base=2)


def parse(bits, start_index):
    version = get_version(bits, start_index)
    type_id = get_type_id(bits, start_index)
    if type_id == 4:
        value, index = get_literal_value(bits, start_index)
        return Literal(version, type_id, value), index
    else:
        packet = Operator(version, type_id, get_length_type_id(bits, start_index))
        if packet.length_type_id == 0:
            bit_length_of_subpackets = get_total_length_of_subpackets_in_bits(bits, start_index)
            index = start_index + 6 + 1 + 15

            while index < start_index + 6 + 1 + 15 + bit_length_of_subpackets:
                subpacket, index = parse(bits, index)
                packet.subpackets.append(subpacket)

        else:
            num_subpackets = get_number_of_subpackets(bits, start_index)
            index = start_index + 6 + 1 + 11
            
            for _ in range(num_subpackets):
                subpacket, index = parse(bits, index)
                packet.subpackets.append(subpacket)

        return packet, index


def main():
    with open(sys.argv[1]) as f:
        bits = f.readline().strip()

    bits = ''.join(f'{int(c, base=16):04b}' for c in bits)
    packet, _ = parse(bits, 0)
    print(packet.eval())


if __name__ == '__main__':
    main()
