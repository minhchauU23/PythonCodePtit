def solve(arr, start, mid, end):
    res = 0
    
    for i in range(start, end):
        if i > mid:
            res += abs(arr[mid] +(i-mid))
        else:
            res += abs(arr[mid] - arr[i])
    return res

test = int(input())
while test > 0:
    test -= 1
    sz = int(input())
    arr = [int(i) for i in input().split()]
    arr = sorted(arr)
    if sz %2 == 0:
        print(min(solve(arr, 0, sz//2, sz), solve(arr, 0, sz//2-1, sz)))
    else:
        print(solve(arr, 0, sz//2, sz))