from decimal import Decimal


class Candidate:
    counter = 1
    def __init__(self, name, theoryScore, practiceScore):
        self.id = 'TS0%d'%Candidate.counter
        self.name = name
        self.theoryScore = theoryScore
        self.practiceScore = practiceScore
        Candidate.counter += 1
    def getAverage(self):
        return Decimal((self.theoryScore + self.practiceScore)/2).quantize(Decimal('1.00'))
    def getStatus(self):
        if self.getAverage() > 9.5:
            return 'XUAT SAC'
        if self.getAverage() >= 8:
            return 'DAT'
        if self.getAverage() >= 5:
            return 'CAN NHAC'
        return 'TRUOT'
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.getAverage(), self.getStatus())

candidates = []
amount = int(input())
for i in range(amount):
    name = input()
    theory = input()
    practice = input()
    if float(theory)> 10: theory = theory[0:1] + "." + theory[1:]
    if float(practice) > 10: practice = practice[0:1] + "." + practice[1:]
    candidates.append(Candidate(name, Decimal(theory), Decimal(practice)))
print(*sorted(candidates, key= lambda item : -item.getAverage()), sep='\n')
# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56

