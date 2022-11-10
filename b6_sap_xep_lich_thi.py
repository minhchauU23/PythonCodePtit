from datetime import datetime


class Monthi:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
    def __str__(self):
        return '{}'.format(self.name)
class CaThi:
    counter = 1
    def __init__(self, date, time, room):
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.time = datetime.strptime(time, '%H:%M')
        self.room = room
        self.id = 'C%03d'%CaThi.counter
        CaThi.counter += 1
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def __str__(self):
        return "%02d/"%self.date.day + "%02d/"%self.date.month + "%04d"%self.date.year + " " +"%02d:"%self.time.hour +  "%02d"%self.time.minute + ' ' + self.room

class LichThi:
    def __init__(self, caThi, monThi, nhom, soLuong):
        self.caThi = caThi
        self.monThi = monThi
        self.nhom = nhom
        self.soLuong = soLuong
    def __str__(self):
        return '{} {} {} {}'.format(self.caThi, self.monThi, self.nhom, self.soLuong)


f = open('MONTHI.in')
size = int(f.readline().strip())
monThi = []
for i in range(size):
    monThi.append(Monthi(f.readline().strip(), f.readline().strip(), f.readline().strip()))
f.close
f = open('CATHI.in')
size = int(f.readline().strip())
caThi = []
for i in range(size):
    caThi.append(CaThi(f.readline().strip(), f.readline().strip(), f.readline().strip()))
f.close()
f = open('LICHTHI.in')
size = int(f.readline().strip())
lichThi = []
for i in range(size):
    arr = f.readline().split()
    ct = None
    for x in caThi:
        if x.id == arr[0]:
            ct = x
            break
    mt = None
    for x in monThi:
        if x.id == arr[1]:
            mt = x
            break
    lichThi.append(LichThi(ct, mt, arr[2], arr[3]))
print(*sorted(lichThi, key= lambda item: (item.caThi.date, item.caThi.time, item.caThi.id)), sep='\n')