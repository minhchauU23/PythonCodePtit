def show(chan, le, arr):
    ic = 0
    il = 0
    for i in range(len(arr)):
        if arr[i] % 2 ==0:
            arr[i] = chan[ic]
            ic += 1
        else:
            arr[i] = le[il]
            il += 1
    return arr


sz = int(input())
arr = []
while len(arr) < sz:
    for i in input().split():
        arr.append(int(i))
chan = []
le = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        chan.append(arr[i])
    else: le.append(arr[i])
print(*show(sorted(chan), sorted(le)[::-1], arr))