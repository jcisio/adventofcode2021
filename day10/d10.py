f = open(__file__[:-3] + '.in', 'r')


scores = [3, 57, 1197, 25137]
chunks = '()[]{}<>'


def calculateCheckerScore(line):
    global scores, chunks
    current_chunk = []
    for i in range(len(line)):
        index = chunks.index(line[i])
        if index % 2 == 0:
            current_chunk.append(line[i])
        elif chunks.index(current_chunk.pop()) != index - 1:
            return scores[index//2]
    return 0


def solvePart1(lines):
    return sum(calculateCheckerScore(line) for line in lines)


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solvePart1(lines))
