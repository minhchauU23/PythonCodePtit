test = int(input())
while test > 0:
    test -= 1
    sz = int(input())
    arr = [int(i) for i in input().split()]
    ct = 0
    for i in range(sz - 1):
        mn = min(arr[i], arr[i+1])
        mx = max(arr[i], arr[i+1])
        while 2 * mn < mx:
              mn *= 2
              ct += 1
    print(ct)