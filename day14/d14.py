from collections import Counter


class Problem:

    def __init__(self):
        self.template = ''
        self.rules = {}

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        lines = f.read().strip().split('\n')
        self.template = lines[0]
        for rule in lines[2:]:
            source, destination = rule.split(' -> ')
            self.rules[source] = destination

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def doStep(self, template):
        new_template = template[0]
        for i in range(len(template) - 1):
            if template[i:i+2] in self.rules:
                new_template += self.rules[template[i:i+2]]
            new_template += template[i+1]
        return new_template

    def solvePart1(self):
        template = self.template
        for i in range(10):
            template = self.doStep(template)
        counter = Counter(template)
        return max(counter.values()) - min(counter.values())

problem = Problem()
problem.solve()
