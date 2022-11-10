import math
prime = [1 for i in range(1001)]

def erathone():
    prime[0] = 0
    prime[1] = 0
    for i in range(4, 1001, 2):
        prime[i] = 0
    for i in range(3, math.isqrt(1001), 2):
        if prime[i] == 1:
            for j in range(i * i, 1001, i):
                prime[j] = 0
erathone()
arr = [int(i) for i in input().split()]
res = []
for row in range(arr[0]):
    tmp = [int(i) for i in input().split()]
    for i in range(arr[1]):
        tmp[i] = prime[tmp[i]]
    res.append(tmp)
for a in res:
    for x in a:
        print(x, end=' ')
    print()


