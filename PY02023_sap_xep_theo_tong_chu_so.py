def sumNB(nb):
    total = 0
    while nb > 0:
        total += nb % 10
        nb //= 10
    return total

test = int(input())
while test >0:
    test -= 1
    amount = int(input())
    arr = [int(i) for i in input().split()]
    ls = list()
    for i in arr:
        ls.append([i, sumNB(i)])
    ls = sorted(ls, key = lambda k: (k[1], k[0]))
    for i in ls:
        print(i[0], end=' ')
    print()
