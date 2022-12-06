f = open("DATA.in")
words = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    for x in line.split():
        try:
            val = int(x)
            if val > 2**32:
                words.append(x)
        except ValueError:
                words.append(x)
f.close()
print(*sorted(words))