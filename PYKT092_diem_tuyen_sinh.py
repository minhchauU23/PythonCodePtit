class ThiSinh:
    counter = 1
    def __init__(self, ten, diem, danToc, khuVuc):
        self.id = "TS%02d"%ThiSinh.counter
        self.ten = ten
        self.diem = diem
        self.danToc = danToc
        self.khuVuc = khuVuc
        ThiSinh.counter += 1
    def getUuTien(self):
        uuTien = 0
        if self.khuVuc == 1:
            uuTien += 1.5
        elif self.khuVuc == 2:
            uuTien += 1

        if self.danToc != "Kinh":
            uuTien += 1.5
        return uuTien

    def getTongDiem(self):
        return self.diem + self.getUuTien()

    def getTrangThai(self):
        if self.diem + self.getUuTien() >= 20.5:
            return "Do"
        return "Truot"

    def __str__(self):
        ht = ""
        for t in self.ten:
            ht += t
            ht += " "
        return "{} {} {} {}".format(self.id, ht.strip(), self.getTongDiem(), self.getTrangThai())


slThiSinh = int(input())
arr = []
for i in range(slThiSinh):
    arr.append(ThiSinh(input().title().split(), float(input()), input(), int(input())))

arr = sorted(arr, key= lambda ts: [-ts.getTongDiem(), ts.id])
for ts in arr:
    print(ts)

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3