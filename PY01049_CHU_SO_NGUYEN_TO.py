
from cmath import sqrt
import math

def isPrime(num):
    num = int(num)
    if num == 2: return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0: return False
    return True

def isGreatPrime(num):
    if isPrime(len(num)) == False: return False
    primes = 0
    for i in range(len(num)):
        if isPrime(int(num[i])): primes += 1
    return primes > len(num)/2
test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print("YES" if isGreatPrime(num) else "NO")
