f = open('d04.in', 'r')


def calculateFinalScore(cards, number):
    for card in cards:
        for i in range(5):
            if sum(card[i::5]) == -5 or sum(card[i*5:i*5+5]) == -5:
                return sum([x for x in card if x != -1]) * number
    return -1

def solvePart1(numbers, cards):
    for number in numbers:
        for card in cards:
            card[:] = [-1 if x==number else x for x in card]
        score = calculateFinalScore(cards, number)
        if score >= 0:
            return score
    return 0


lines = f.read().strip().split('\n')
numbers = list(map(int, lines.pop(0).split(',')))
cards = [list(map(int, ' '.join(lines[i*6+1:i*6+6]).split())) for i in range(len(lines)//6)]
print("Puzzle 1: ", solvePart1(numbers, cards))
