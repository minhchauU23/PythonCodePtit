

lines = int(input())
words = {}
s = ''
for i in range(lines):
    line = input().lower() + ' '
    for j in range(len(line)):
        if not line[j].isalpha():
            if s != '':
                if s in words:
                    words[s] += 1
                else: words[s] = 1
                s = ''
        else: s+= line[j]
words = sorted(words.items(), key= lambda x:(-x[1], x[0]))
for x in words:
    print(x[0], x[1])
# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.