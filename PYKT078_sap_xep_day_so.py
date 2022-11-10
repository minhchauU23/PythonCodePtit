
test = int(input())
while test > 0:
    test -= 1
    n, m = input().split()
    ls = [int(i) for i in input().split()]
    index = 0
    for i in range(0, len(ls)):
        if(ls[index] < ls[i]): index = i
    ls.insert(index, int(m))
    res = []
    for i in ls:
        if i < 0:
            res.append(i)
    for i in ls:
        if i >= 0:
            res.append(i)
    print(*res)