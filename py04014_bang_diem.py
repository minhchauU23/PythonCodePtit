

from math import ceil


class Student:
    counter = 1
    def __init__(self, name, scores):
        self.id = 'HS' + str.format("%02d"%Student.counter)
        self.name = name
        self.scores = scores
        Student.counter += 1
    def getAverage(self):
        average = 0
        for i in range(len(self.scores)):
            if i == 0 or i == 1:
                average += self.scores[i]
            average += self.scores[i]
        return round(average/10/1.2, 1)
    def getRank(self):
        average = self.getAverage()
        if average >= 9: return 'XUAT SAC'
        if average >= 8: return 'GIOI'
        if average >= 7: return 'KHA'
        if average >= 5: return 'TB'
        return 'YEU'
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.getAverage(), self.getRank())

studenstList = []
amount = int(input())
for i in range(amount):
    name = input().strip()
    scores = [float(x) for x in input().split()]
    studenstList.append(Student(str.title(name), scores))
studenstList.sort(key = lambda item : -item.getAverage())
print(*studenstList,sep='\n')

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0