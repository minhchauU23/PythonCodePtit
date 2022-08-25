def isIncrsAndDecrsNumber(num):
    if len(num) < 3: return "NO"
    l, r = 0, len(num) - 1
    while l < r:
        if num[l] < num[l + 1]:
            l += 1
        elif num[r] < num[r-1]:
            r-=1
        else: break
    if l==r: return "YES"
    return "NO"

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print(isIncrsAndDecrsNumber(num))