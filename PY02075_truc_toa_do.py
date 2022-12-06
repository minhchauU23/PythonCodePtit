
test = int(input())
while test > 0:
    test -= 1
    numOfEdge = int(input())
    edges = []
    for i in range(numOfEdge):
        edges.append([int(i) for i in input().split()])
    edges = sorted(edges, key= lambda k: (k[1], k[0]))
    ct = 1
    lastIndex = 0
    for id in range(1, len(edges)):
        if edges[id][0] >= edges[lastIndex][1]:
            lastIndex = id
            ct += 1
    print(ct)


# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40