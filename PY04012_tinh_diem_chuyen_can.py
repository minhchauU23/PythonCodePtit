class Student:
    def __init__(self, sID, name, classs):
        self.sID = sID
        self.name = name
        self.classs = classs
        self.attendanceScore = 10

    def setAttendanceScore(self, attendanceTable):
        attendance = 10
        for day in range(len(attendanceTable)):
            if attendanceTable[day] == "v":
                attendance -= 2
            elif attendanceTable[day] == "m":
                attendance -= 1
        self.attendanceScore = max(attendance, 0)

    def getNotice(self):
        if self.attendanceScore == 0:
            return "KDDK"
        return ""

    def __str__(self):
        return "{} {} {} {} {}".format(self.sID, self.name, self.classs, self.attendanceScore, self.getNotice())


numOfStudents = int(input())
students = dict()
for i in range(numOfStudents):
    std = Student(input(), input(), input())
    students[std.sID] = std

for i in range(numOfStudents):
    attendance = input().split()
    students[attendance[0]].setAttendanceScore(attendance[1])

for sId in students:
    print(students[sId])

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm