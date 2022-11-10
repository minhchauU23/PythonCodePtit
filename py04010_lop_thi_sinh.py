class Student:
    def __init__(self, name, birthDay, firstScore, secondScore, thirdScore):
        self.name = name
        self.birthDay = birthDay
        self.firstScore = firstScore
        self.secondScore = secondScore
        self.thirdScore = thirdScore
    
    def getTotalScore(self):
        return self.firstScore + self.secondScore + self.thirdScore

    def __str__(self):
        return '{} {} {}'.format(self.name, self.birthDay, str.format("%.01f" %self.getTotalScore()))

print(Student(input(), input(), float(input()), float(input()), float(input())))
