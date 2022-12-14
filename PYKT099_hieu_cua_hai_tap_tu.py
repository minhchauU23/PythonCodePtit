
f1 = open("DATA1.in", "r")
ls1 = set()
while True:
    x = f1.readline()
    if x == "":
        break
    else:
        for word in x.lower().split():
            ls1.add(word)

f2 = open("DATA2.in", "r")
ls2 = set()
while True:
    line = f2.readline()
    if line == "":
        break
    for word in line.lower().split():
        ls2.add(word)

diff1 = ls1.difference(ls2)
diff2 = ls2.difference(ls1)
diff1 = sorted(diff1)
diff2 = sorted(diff2)
print(*diff1)
print(*diff2)