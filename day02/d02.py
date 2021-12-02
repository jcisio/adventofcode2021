f = open('d02.in', 'r')


def findResult(lines):
    position = 0
    depth = 0
    for line in lines:
        (direction, amount) = line.split()
        amount = int(amount)
        if direction == 'down':
            depth += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'forward':
            position += amount
    return position * depth


lines = f.read().strip().split('\n')
print("Puzzle 1: ", findResult(lines))
