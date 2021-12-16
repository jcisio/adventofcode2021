class Packet:

    bits = []
    version = 0
    type = 0
    data = {}
    # For literal packets, data contains the literal 'value'
    # For operator packets, data contains length_type_id, length and packets.

    def __init__(self, bits):
        self.bits = bits
        print('Initializing packet with bits:', self.bits)

    # Parses data and returns the number of bits in the packet
    def parse(self):
        self.version = int(self.bits[:3], 2)
        self.type = int(self.bits[3:6], 2)
        if self.type == 4:
            self.data['value'] = 0
            i = 6
            while True:
                self.data['value'] = self.data['value'] * 16 + int(self.bits[i+1:i+5], 2)
                i += 5
                if self.bits[i-5] == '0':
                    break
        else:
            self.data['length_type_id'] = int(self.bits[6], 2)
            if self.data['length_type_id'] == 0:
                i = 7 + 15
                self.data['length_bits'] = int(self.bits[7:i], 2)
            else:
                i = 7 + 11
                self.data['length_packets'] = int(self.bits[7:i], 2)
            self.data['packets'] = []
            header_length = i
            while True:
                packet = Packet(self.bits[i:])
                self.data['packets'].append(packet)
                i += packet.parse()
                if self.data['length_type_id'] == 0:
                    if self.data['length_bits'] == i - header_length:
                        break
                elif self.data['length_type_id'] == 1:
                    if self.data['length_packets'] == len(self.data['packets']):
                        break
        return i

class Problem:

    packet = None

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        data = f.read().strip()
        self.packet = Packet(''.join('{:04b}'.format(int(x, 16)) for x in data))

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def sumVersion(self, packet):
        version = packet.version
        if packet.data['packets']:
            for p in packet.data['packets']:
                version += self.sumVersion(p)
        return version

    def solvePart1(self):
        self.packet.parse()
        return self.sumVersion(self.packet)


problem = Problem()
problem.solve()
