n, m, k = [int(i) for i in input().split()]
gifts = dict()
id = 1
for i in input().split():
    gifts.update({id:int(i)})
    id += 1

gifts = {key:val for key,val in sorted(gifts.items(), key=lambda it: it[1])}

check = [0 for i in range(n + 1)]
common = []
T = int(input())
for i in input().split():
    check[int(i)] = 1

te = int(input())
for i in input().split():
    if check[int(i)] == 1:
        common.append(i)
if  m < k or k > len(common):
    print(-1)
else:
    common = sorted(common, key = lambda it: gifts[it])
    result = 0
    for i in range(k):
        result += gifts[common[i]]
        gifts[common[i]] = None
