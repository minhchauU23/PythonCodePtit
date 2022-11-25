import math

def isPalindrome(s):
    if s == s[::-1] and len(s) > 1:
        return True
    return False


row, col = input().split()

grid = []
mx = -1
for i in range(int(row)):
    r = input().split()
    for i in r:
        if isPalindrome(i):
            if mx == -1:
                mx = int(i)
            else:
                mx = max(mx, int(i))
    grid.append(r)

if mx == -1:
    print("NOT FOUND")
else:
    print(mx)
    for i in range(int(row)):
        for j in range(int(col)):
            if int(grid[i][j]) == mx:
                print("Vi tri [{}][{}]".format(i, j))

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77