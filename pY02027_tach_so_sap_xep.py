import re
sz = int(input())
numbers = []
for i in range(sz):
    line = input()
    nb = ""
    for i in range(len(line)):
        if line[i].isdigit():
            nb += line[i]
        elif nb != "":
            numbers.append(int(nb))
            nb = ""
    if nb != "":
        numbers.append(int(nb))
        nb = ""
numbers = sorted(numbers, key=lambda it: it)
print(*numbers, sep= "\n")

# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa
