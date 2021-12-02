f = open('d01.in', 'r')


def findMeasurementIncreases(lines):
    return sum(1 if lines[i] < lines[i+1] else 0 for i in range(len(lines)-1))


lines = list(map(int, f.read().strip().split('\n')))
print("Puzzle 1: ", findMeasurementIncreases(lines))
