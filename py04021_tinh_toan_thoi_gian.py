

from datetime import datetime


class Gamer:
    def __init__(self, id, name, checkIn, checkOut):
        self.id = id
        self.name = name
        self.checkIn = checkIn
        self.chekOut = checkOut
    def getTime(self):
        diff = self.chekOut - self.checkIn
        return diff.total_seconds()
    def __str__(self):
        seconds = int(self.getTime())
        hour = seconds//3600
        minute = (seconds - hour * 3600)//60
        return '{} {} {} gio {} phut'.format(self.id, self.name, hour, minute)

gamers = []
amount = int(input())
for i in range(amount):
    gamers.append(Gamer(input(), input(), datetime.strptime(input().strip(), '%H:%M'), datetime.strptime(input().strip(), '%H:%M')))
print(*sorted(gamers, key= lambda item : -item.getTime()), sep='\n')

# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00