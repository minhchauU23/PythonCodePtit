import math

row, col = input().split()

grid = []
mx = -1
mn = 100000
for i in range(int(row)):
    r = [int(i) for i in input().split()]
    for i in r:
        mx = max(mx, i)
        mn = min(mn, i)
    grid.append(r)

ok = False
position = []
for i in range(int(row)):
    for j in range(int(col)):
        if grid[i][j] == mx - mn:
            ok = True
            position.append([i, j])
if ok:
    print(mx -mn)
    for a in position:
        print("Vi tri [{}][{}]".format(a[0], a[1]))
else:
    print("NOT FOUND")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77