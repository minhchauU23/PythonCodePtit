import math


def  isPrime(nb):
    if nb == 2:
        return True
    if nb < 2 or nb % 2 == 0:
        return False
    for i in range(3, math.isqrt(nb) + 1, 2):
        if nb % i == 0:
            return  False
    return  True

sz = int(input())
arr = [int(i) for i in input().split()]
b = []
for i in range(len(arr)):
    if arr[i] not in b:
        b.append(arr[i])

res = -1
for i in range(len(b)):
    s1 = sum(b[0:i+1])
    s2 = sum(b[i+1:])
    if isPrime(s1) and isPrime(s2):
        res = i
        break
print(res if res != -1 else "NOT FOUND")