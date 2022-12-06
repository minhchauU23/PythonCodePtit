from decimal import Decimal

class Candidate:
    counter = 1
    def __init__(self, name, idAdmiss, firstScore, secondScore):
        self.id = "GV%02d"%Candidate.counter
        self.name = name
        self.idAdmiss = idAdmiss
        self.firstScore = firstScore
        self.secondScore = secondScore
        Candidate.counter += 1

    def getPriorityScore(self):
        if self.idAdmiss[1] == "1":
            return Decimal(2.0)
        if self.idAdmiss[1] == "2":
            return Decimal(1.5)
        if self.idAdmiss[1] == "3":
            return Decimal(1)
        return Decimal(0)

    def getSubject(self):
        if self.idAdmiss[0] == "A":
            return "TOAN"
        if self.idAdmiss[0] == "B":
            return "LY"
        return "HOA"

    def getTotalScore(self):
        return self.firstScore * 2 + self.secondScore + self.getPriorityScore()

    def getStatus(self):
        if self.getTotalScore() >= 18:
            return "TRUNG TUYEN"
        return "LOAI"

    def __str__(self):
        return "{} {} {} {} {}".format(self.id, self.name, self.getSubject(), Decimal(self.getTotalScore()).quantize(Decimal("1.0")), self.getStatus())


nbOfCandidates = int(input())
candidates = []
for cd in range(nbOfCandidates):
    candidates.append(Candidate(input().strip(), input().strip(), Decimal(input().strip()), Decimal(input().strip())))
candidates = sorted(candidates, key=lambda it: -it.getTotalScore())
print(*candidates, sep="\n")

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0