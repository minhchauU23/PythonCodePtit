def getCommon(a1, a2, a3):
    common = []
    k1 = k2 = k3 = 0
    while k1 < len(a1) and k2 < len(a2) and k3 < len(a3):
        if a1[k1] < a2[k2]:
            k1 += 1
        elif a1[k1] > a2[k2]:
            k2 += 1
        else:
            if a3[k3] < a2[k2]:
                k3 += 1
            elif a3[k3] > a2[k2]:
                k1 += 1
                k2 += 1
            else:
                common.append(a3[k3])
                k1 += 1
                k2 += 1
                k3 += 1
    return common

test = int(input())
while test > 0:
    test -= 1
    s1, s2, s3 = input().split()
    a1 = [int(i) for i in input().split()]
    a2 = [int(i) for i in input().split()]
    a3 = [int(i) for i in input().split()]
    common = getCommon(a1, a2, a3)
    if len(common) == 0: print("NO")
    else: print(*common)

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9