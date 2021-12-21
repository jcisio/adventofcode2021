class Die:

    def __init__(self):
        self.current = 0
        self.rolls = 0

    def roll(self):
        self.current = (self.current % 100) + 1
        self.rolls += 1
        return self.current


class Problem:

    def __init__(self):
        self.players = [
            {'position': 0, 'score': 0},
            {'position': 0, 'score': 0},
        ]

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        for i, line in enumerate(f.read().strip().split('\n')):
            _, p = line.split(': ')
            self.players[i]['position'] = int(p)

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def solvePart1(self):
        current_player = 0
        die = Die()
        while True:
            next = die.roll() + die.roll() + die.roll()
            self.players[current_player]['position'] = (self.players[current_player]['position'] + next - 1) % 10 + 1
            self.players[current_player]['score'] += self.players[current_player]['position']
            if self.players[current_player]['score'] >= 1000:
                break
            current_player = 1 - current_player
        return die.rolls * self.players[1 - current_player]['score']


problem = Problem()
problem.solve()
