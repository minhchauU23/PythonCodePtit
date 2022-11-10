def solve(arr):
    cnt = 0
    while not (arr[0] == arr[1] == arr[2] == arr[3]):
        cnt += 1
        for i in range(0, 4):
            arr[i] = abs(arr[i] - arr[i+1])
        arr[4] = arr[0]
    return cnt


while True:
    arr = []
    ok = False
    for i in input().split():
        arr.append(int(i))
        if int(i) != 0:
            ok = True
    if not ok: break
    arr.append(arr[0])
    print(solve(arr))