

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

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    num = num[max(0, len(num)-4):]
    print("YES" if isPrime(num) else "NO")
