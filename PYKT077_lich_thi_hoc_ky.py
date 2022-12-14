from datetime import datetime

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return "{} {}".format(self.id, self.name)

class TestSchedule:
    counter = 1
    def __init__(self, subject, date, time, group):
        self.id = "T%03d"%TestSchedule.counter
        self.subject = subject
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.time = datetime.strptime(time, "%H:%M")
        self.group = group
        TestSchedule.counter += 1
    def __str__(self):
        return "{} {} {} {} {}".format(self.id, self.subject, datetime.strftime(self.date, "%d/%m/%Y"), datetime.strftime(self.time,"%H:%M"), self.group)


n, m = [int(i) for i in input().split()]
subjectDict = dict()
for i in range(n):
    subject = Subject(input().strip(), input().strip())
    subjectDict.update({subject.id : subject})

testSchedules = []
for i in range(m):
    testSchedule = input().split()
    testSchedules.append(TestSchedule(subjectDict[testSchedule[0]], testSchedule[1], testSchedule[2], testSchedule[3]))

testSchedules = sorted(testSchedules, key = lambda it: [it.date, it.time, it.subject.id])
for test in testSchedules:
    print(test)

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05