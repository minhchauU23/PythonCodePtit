size = int(input())
arr =  [int(i) for i in input().split()]

res = 1000000000000
for i in range(size):
    ok = True
    diff = 0
    for j in range(size):
        if arr[i] - abs(i - j) <= 0:
            ok = False
            break
        diff += abs(arr[j] - arr[i] + abs(i-j))
    if ok:
        res = min(res, diff)
print(res)