import datetime


class TestSchedule:
    counter = 1
    def __init__(self, date, time, room):
        self.id = "C%03d"%TestSchedule.counter
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.time = datetime.datetime.strptime(time, "%H:%M")
        self.room = room
        TestSchedule.counter += 1
    def __str__(self):
        return "{} {} {} {}".format(self.id, self.date.strftime("%d/%m/%Y"), self.time.strftime("%H:%M"), self.room)


f = open("CATHI.in", "r")
schedule = []
numOfSchedule = f.readline().strip()
for i in range(int(numOfSchedule)):
    schedule.append(TestSchedule(f.readline().strip(), f.readline().strip(), f.readline().strip()))
schedule = sorted(schedule, key= lambda it: (it.date, it.time, it.id))
print(*schedule, sep="\n")