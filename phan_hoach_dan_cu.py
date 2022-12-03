test = int(input())

while test > 0:
    test -= 1
    n, c, d = [int(i) for i in input().split()]
    if c > d:
        c = c + d
        d = c - d
        c = c - d
    ps = [int(i) for i in input().split()]
    ps = sorted(ps)[::-1]
    s1 = sum(ps[:c])
    s2 = sum(ps[c:c+d])
    print("%06f"%(s1/c + s2/d))
