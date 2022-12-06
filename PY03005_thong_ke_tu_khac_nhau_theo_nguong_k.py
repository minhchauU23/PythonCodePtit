import re

words = dict()
nbLines, k = [int(i) for i in input().split()]
for i in range(nbLines):
    line = str(input().lower())
    for word in re.split(r"[,.?!:;()-/\s]\s*", line):
        if word != "":
            if word in words:
                words[word] += 1
            else:
                words.update({word: 1})

words = sorted(words.items(), key= lambda k: (-k[1], k[0]))
for word in words:
    if word[1] >= k:
        print(*word, sep= " ")

# 3 2
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
