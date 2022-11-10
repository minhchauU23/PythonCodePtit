from math import isqrt


table = [True for i in range(1000001)]
prime = [2]
def erathone():
    table[0] = table[1] = False
    for i in range(4, 1000001, 2):
        table[i] = False
    for i in range(3, isqrt(1000001), 2):
        if table[i]:
            prime.append(i)
            for j in range(i*i, 1000001, i):
                table[j] = False
    for i in range(isqrt(1000001) + 1 , 1000001, 2):
        if table[i]:
            prime.append(i)
erathone()
n, x = [int(i) for i in input().split()]
for i in range(n + 1):
    print(x, end= ' ')
    x += prime[i]

