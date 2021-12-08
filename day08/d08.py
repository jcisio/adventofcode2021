f = open('d08.in', 'r')


def solvePart1(data):
    return sum(sum(1 if len(digit) in [2,3,4,7] else 0 for digit in item[1].split()) for item in data)


data = [line.split('|') for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solvePart1(data))
