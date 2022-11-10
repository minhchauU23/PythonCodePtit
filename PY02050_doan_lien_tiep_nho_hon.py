
from inspect import stack


test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    arr = [int(i) for i in input().split()]
    res = [1 for i in range(size)]
    stk = []
    stk.append(-1)
    for i in range(size):
        while len(stk) > 1:
            x = stk.pop()
            if arr[x] > arr[i]:
                stk.append(x)
                break
        x = stk.pop()
        res[i] = i - x
        stk.append(x)
        stk.append(i)
    print(*res)
