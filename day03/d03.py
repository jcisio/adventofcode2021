f = open('d03.in', 'r')


def findPowerConsumption(lines):
    gamma, epsilon = 0, 0
    for i in range(len(lines[0])):
        nbits = sum([int(line[i]) for line in lines])
        major_bit = 1 if nbits > len(lines)/2 else 0
        gamma = gamma*2 + major_bit
        epsilon = epsilon*2 + (1 - major_bit)
    return gamma * epsilon

lines = f.read().strip().split('\n')
print("Puzzle 1: ", findPowerConsumption(lines))
