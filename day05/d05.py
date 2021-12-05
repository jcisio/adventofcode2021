f = open('d05.in', 'r')


def findDangerousAreas(vents):
    Nmax = max([max(vent) for vent in vents]) + 1
    map = [[0]*Nmax for i in range(Nmax)]
    for vent in vents:
        if vent[0] != vent[2] and vent[1] != vent[3]:
            continue
        if vent[0] == vent[2]:
            for i in range(min(vent[1::2]), max(vent[1::2]) + 1):
                map[i][vent[0]] += 1
        elif vent[1] == vent[3]:
            for i in range(min(vent[0::2]), max(vent[0::2]) + 1):
                map[vent[1]][i] += 1
    return sum([sum([1 for x in line if x >= 2]) for line in map])

vents = [list(map(int, line.replace(' -> ', ',').split(','))) for line in f.read().strip().split('\n')]
print("Puzzle 1: ", findDangerousAreas(vents))
