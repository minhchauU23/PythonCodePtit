
def minTriple(arr):
    sz = len(arr)
    if sz <= 3:
        sum(arr)
    min1 = 1e8 + 2
    min2 = 1e8 + 1
    min3 = 1e8
    for i in range(sz):
        if arr[i] < min3:
            min1 = min2
            min2 = min3
            min3 = arr[i]
        elif arr[i] < min2:
            min1 = min2
            min2 = arr[i]
        elif arr[i] < min1:
            min1 = arr[i]
    return min1 + min2 + min3

test = int(input())
while test > 0:
    test -= 1
    sz = int(input())
    arr = [int(nb) for nb in input().split()]
    print(minTriple(arr))