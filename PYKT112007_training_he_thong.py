from decimal import Decimal
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    k = Decimal(input())
    arr = [Decimal(i) for i in input().split()]
    arr.append(Decimal("1.0000"))
    arr = sorted(arr)
    id = 0
    while id < n and k > Decimal("0"):
        if arr[id] != arr[id + 1]:
            diff = arr[id + 1] - arr[id]
            if k >= diff * Decimal(id + 1):
                for i in range(0, id + 1):
                    arr[i] = arr[id + 1]
                k -= diff * Decimal(id + 1)
            else:
                diff = k/Decimal(id + 1)
                for i in range(0, id + 1):
                    arr[i] += diff
                k = 0
        id += 1
    mul = Decimal(1)
    for i in range(n):
        mul *= arr[i]
    print(mul.quantize(Decimal("1.000000")))

# 2
# 4
# 1.4000
# 0.5000 0.7000 0.8000 0.6000
# 2
# 1.0000
# 0.0000 0.0000