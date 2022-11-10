import math


prime = [True for i in range(1000001)]

def erathone():
    prime[0] = False
    prime[1] = False
    for i in range(4, 1000001, 2):
        prime[i] = False
    for i in range(3, math.isqrt(1000001), 2):
        if prime[i]:
            for j in range(i * i, 1000001, i):
                prime[j] = False

erathone()
amount = int(input())
mp = dict()
ls = [int(i) for i in input().split()]
for i in ls:
    if prime[i] == True:
        if i in mp:
            mp[i] += 1
        else:
            mp.update({i:1})
for i in mp:
    print(i, mp[i])
