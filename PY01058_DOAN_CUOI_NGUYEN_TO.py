
from math import isqrt


def isPrime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    for i in range(3, isqrt(num), 2):
        if num % i == 0:
            return False
    return True

test = int(input())
while test > 0:
    test -= 1
    s = str(input())
    num = int(s[len(s)-4:])
    print("YES" if isPrime(num) else "NO")