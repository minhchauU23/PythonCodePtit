def getMinStep(N, X, Y, Z, arr):
    if N == 1:
        return X
    if N % 2 == 0:
        if arr[N-1] == None:
            arr[N-1] = getMinStep(N-1, X, Y, Z, arr)
        if arr[N//2] == None:
            arr[N//2] = getMinStep(N//2, X, Y, Z, arr)
        arr[N] = min(arr[N-1] + X, arr[N//2] + Z)
        return arr[N]
    if arr[N-1]  == None:
        arr[N - 1] = getMinStep(N - 1, X, Y, Z, arr)
    if arr[N // 2] == None:
        arr[N // 2] = getMinStep(N // 2, X, Y, Z, arr)
    if arr[N//2 + 1] == None:
        arr[N//2 + 1] = getMinStep(N//2 + 1, X, Y, Z, arr)
    arr[N] = min(arr[N-1] + X, min( arr[N//2] + Z + X, arr[N//2 + 1] + Y + Z))
    return arr[N]

test = int(input())
while test > 0:
    test -= 1
    N = int(input())
    X, Y, Z = [int(i) for i in input().split()]
    arr = [None for i in range(200)]
    print(getMinStep(N, X, Y, Z, arr))