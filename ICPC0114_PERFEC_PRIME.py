
from math import isqrt


def isPrime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, isqrt(num), 2):
        if num % i == 0:
            return False
    return True

def isPerfectPrime(num):
    return isPrime(num) and isPrime(sum(map(int,str(num)))) and isPrime(int(str(num)[::-1]))

test = int(input())
while test > 0:
    test -= 1
    num = int(input())
    print("Yes" if isPerfectPrime(num) else "No")
