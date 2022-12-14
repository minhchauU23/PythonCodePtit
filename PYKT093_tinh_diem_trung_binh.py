import datetime
import decimal
from decimal import Decimal
class Student:
    counter = 1
    def __init__(self, name, firstScore, secondScore, thirdScore):
        self.id = "SV%02d"%Student.counter
        self.name = name
        self.firstScore = firstScore
        self.secondScore = secondScore
        self.thirdScore = thirdScore
        Student.counter += 1

    def setRank(self, rank):
        self.rank = rank

    def getAverage(self):
        average = Decimal((self.firstScore*3 + self.secondScore*3 + self.thirdScore*2)/8)
        return Decimal.quantize(average, Decimal("1.00"), decimal.ROUND_HALF_UP)

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.name, self.getAverage(), self.rank)


numOfStudents = int(input())
students = []
for i in range(numOfStudents):
    name = input().title().split()
    roleName = ""
    for n in name:
        roleName += n + " "
    students.append(Student(roleName.strip(), Decimal(input()), Decimal(input()), Decimal(input())))


students = sorted(students, key= lambda st: -st.getAverage())
rank = 2
average = students[0].getAverage()
students[0].setRank(1)
for i in range(1, len(students)):
    if students[i].getAverage() == students[i-1].getAverage():
        students[i].setRank(students[i-1].rank)
    else:
        students[i].setRank(rank)
    rank += 1
print(*students, sep= "\n")

# 3
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 7
# Tran    THI  HAO
# 5
# 5
# 5