from datetime import date, datetime


class Weather:
    counter = 1
    def __init__(self, place, totalTime, rain):
        self.id = 'T' + str.format("%02d" %Weather.counter)
        self.place = place
        self.totalTime = totalTime
        self.rain = rain
        Weather.counter+=1

    def update(self, diffTime, rain):
        self.totalTime += diffTime
        self.rain += rain

    def __str__(self):
        return '{} {} {}'.format(self.id ,self.place, self.getAverageRain())

    def getAverageRain(self):
        return self.rain * 3600/self.totalTime
    
class WeatherDict(dict):
    def __getitem__(self, key):
        value = self[key] = type(self)()
        return value

wtdct = WeatherDict()
amount = int(input())
for i in range(amount):
    name = input()
    diff = datetime.strptime(input().strip(), '%H:%M') - datetime.strptime(input().strip(), '%H:%M')
    rain = int(input())
    if wtdct[name] is None:
        wtdct.update(name, Weather(name, diff.total_seconds(), rain))
    else:
        wtdct.get(name).update(diff, rain)
for i in wtdct:
    print(i, wtdct[i])
        
        


# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35