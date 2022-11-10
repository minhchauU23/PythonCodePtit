import math


def isPrime(nb):
    if nb == 2: return True
    if nb < 2 or nb % 2 == 0:
        return False
    for i in range(2, math.isqrt(nb) + 1):
        if nb % i == 0:
            return False
    return True

sz = int(input())
arr = [int(i)for i in input().split()]
primes = []
for i in range(len(arr)):
    if isPrime(arr[i]):
        primes.append(arr[i])
        arr[i] = False
primes = sorted(primes)
id = 0
for i in range(len(arr)):
    if arr[i] is False:
        arr[i] = primes[id]
        id += 1
print(*arr)