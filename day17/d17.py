import re


class Problem:

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        m = re.search(r'x=([0-9\-]+)\.\.([0-9\-]+), y=([0-9\-]+)\.\.([0-9\-]+)', f.read().strip())
        self.target = list(map(int, m.groups()))

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def findVx(self):
        for vx in range(1, self.target[1] + 1):
            x = 0
            vx_init = vx
            while x < self.target[0] and vx > 0:
                x += vx
                if self.target[0] <= x <= self.target[1]:
                    break
                vx = vx - 1
            if vx > 0:
                break
        return vx_init

    def solvePart1(self):
        vx = self.findVx()
        vy = -1 - self.target[2]
        return vy*(vy+1)//2

problem = Problem()
problem.solve()
