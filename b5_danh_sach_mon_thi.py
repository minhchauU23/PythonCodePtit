class Exam:
    def __init__(self, id, name, kind):
        self.id = id
        self.name = name
        self.kind = kind
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.kind)

exams = []
amount = int(input())
for i in range(amount):
    exams.append(Exam(input(), input(), input()))

print(*sorted(exams, key= lambda item: item.id), sep = '\n')
# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen