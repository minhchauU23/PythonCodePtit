import math


size = int(input())
row = [0 for i in range(size)]
col = [0 for i in range(size)]
for i in range(size):
    line = str(input())
    for j in range(size):
        if line[j] == 'C':
            row[i] += 1
            col[j] += 1
res = 0
for i in range(size):
    if row[i] > 0:
        res += math.comb(row[i], 2)
    if col[i] > 0:
        res += math.comb(col[i], 2)
print(res)
