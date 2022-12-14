
class PhongBan:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name

class NhanVien:
    grid = [[10, 12, 14, 20], [10, 11, 13, 16], [9, 10, 12, 14], [8, 9, 11, 13]]
    def __init__(self, id, ten, luongCoBan, ngayCong):
        self.id = id
        self.ten = ten
        self.luongCoBan = luongCoBan
        self.ngayCong = ngayCong
    def setPhongBan(self, phongBan):
        self.phongBan = phongBan

    def getLuong(self):
        namCongTac = int(self.id[1:3])
        col = 0
        if namCongTac >= 4 and namCongTac <= 8:
            col = 1
        elif namCongTac >= 9 and namCongTac <= 15:
            col = 2
        elif namCongTac >= 16:
            col = 3
        return self.luongCoBan * self.ngayCong * NhanVien.grid[ord(self.id[0]) -ord("A")][col] * 1000

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.ten, self.phongBan, self.getLuong())

slPB = int(input())
pb = dict()
for i in range(slPB):
    line = input().split()
    name = ""
    for n in range(1, len(line)):
        name += line[n] + " "
    pb.update({line[0]:PhongBan(line[0],name.strip() )})

slNV = int(input())
nvs = []
for i in range(slNV):
    nvs.append(NhanVien(input().strip(), input().strip(), int(input()), int(input())))

for nv in nvs:
    nv.setPhongBan(pb[nv.id[-2::]])
    print(nv)

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24