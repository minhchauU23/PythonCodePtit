from itertools import combinations

n, k = input().split()
arr = set(input().split())

for ls in combinations(sorted(arr), int(k)):
    print(*ls)