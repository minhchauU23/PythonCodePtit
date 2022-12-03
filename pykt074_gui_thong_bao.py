import math

test = int(input())
while test > 0:
    test -= 1
    mess = input()
    if len(mess) <= 100:
        print(mess)
    else:
        id = 100
        while mess[id] != " ":
            id -= 1
        print(mess[:min(id, 99)])
# 2
# Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
# Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen
