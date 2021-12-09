f = open('d09.in', 'r')


def findLowPoints(map):
    low_points = []
    for y in range(len(map)-2):
        for x in range(len(map[y])-2):
            if map[y+1][x+1] < min(map[y+1][x], map[y][x+1], map[y+1][x+2], map[y+2][x+1]):
                low_points.append(int(map[y+1][x+1]))
    return sum(low_points) + len(low_points)



map = f.read().strip().split('\n')
# Add border for easy indexing.
map = ['A'*(len(map[0])+2)] + ['A'+line+'A' for line in map] + ['A'*(len(map[0])+2)]
print("Puzzle 1: ", findLowPoints(map))
