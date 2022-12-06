import datetime
import decimal
import re
from decimal import  Decimal
class Racer:
    def __init__(self, name, local, finishTime):
        self.name = name
        self.local = local
        self.startTime = datetime.datetime.strptime("6:00", "%H:%M")
        self.finishTime = datetime.datetime.strptime(finishTime, "%H:%M")
        self.distance = 120
    def getSpeed(self):
        diff = self.finishTime - self.startTime
        speed = Decimal(self.distance/(diff.total_seconds()/3600))
        return speed.quantize(Decimal("1"))
    def getID(self):
        s = self.local + " " + self.name
        s = re.split("\\s+", s)
        result = ""
        for si in s:
            result += si[0].upper()
        return result
    def __str__(self):
        return "{} {} {} {}".format(self.getID(), self.name, self.local, str(self.getSpeed()) +" Km/h")

numOfRacers = int(input())
racers = []
for i in range(numOfRacers):
    racers.append(Racer(input(), input(), input()))
racers = sorted(racers, key= lambda rc: rc.finishTime )
print(*racers, sep='\n')

# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45