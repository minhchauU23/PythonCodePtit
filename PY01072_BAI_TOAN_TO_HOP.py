from itertools import combinations

n, k = [int(i) for i in input().split()]
ls = [int(i) for i in input().split()]
arr = list()
for i in ls:
    if i not in arr:
        arr.append(i)

for item in combinations(sorted(arr), k):
    print(*item)

