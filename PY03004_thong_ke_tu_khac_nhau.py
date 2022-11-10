from curses.ascii import isalnum, isalpha, isdigit


n = int(input())
word = dict()
for i in range(n):
    arr = input().lower().split()
    for x in arr:
        s = ''
        for i in x:
            if isalpha(i) or isdigit(i):
                s += i
            else:
                if s != "":
                    if s in word:
                        word[s]+=1
                    else: word.update({s : 1})
                s =""
        if s != '':
            if s in word:
                word[s]+=1
            else: word.update({s : 1})
sortWord = sorted(word.items(), key=lambda kv: (-kv[1], kv[0]))
for i in sortWord:
    print(*i)


# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.