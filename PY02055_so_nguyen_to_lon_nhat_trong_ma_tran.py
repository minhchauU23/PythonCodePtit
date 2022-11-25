import math


def isPrime(nb):
    if nb == 2 : return True
    if nb < 2 or nb % 2 == 0:
        return False
    for i in range(3, math.isqrt(nb) + 1, 2):
        if nb % i == 0:
            return False
    return True
row, col = input().split()

grid = []
mx = -1
for i in range(int(row)):
    r = [int(i) for i in input().split()]
    for i in r:
        if isPrime(i):
            if mx == -1:
                mx = i
            else:
                mx = max(mx, i)
    grid.append(r)

if mx == -1:
    print("NOT FOUND")
else:
    print(mx)
    for i in range(int(row)):
        for j in range(int(col)):
            if grid[i][j] == mx:
                print("Vi tri [{}][{}]".format(i, j))

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29