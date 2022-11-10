

test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    table = dict()
    res = -1
    for i in input().split():
        if int(i) not in table:
            table[int(i)] = 1
        else: table[int(i)] = table[int(i)] + 1
        if res == -1 or table[res] < table[int(i)]:
            res = int(i)
    print(res if table[res] > n/2 else "NO")
