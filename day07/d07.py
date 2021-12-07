import statistics

f = open('d07.in', 'r')


def findMinimumFuel(positions):
    median = int(statistics.median(positions))
    return sum([abs(x - median) for x in positions])


positions = list(map(int, f.read().strip().split(',')))
print("Puzzle 1: ", findMinimumFuel(positions))
