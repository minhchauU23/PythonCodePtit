from math import isqrt


def isprime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, isqrt(num), 2):
        if num % i == 0:
            return False
    return True

def sumOfElement(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

test = int(input())
while test > 0:
    test -= 1
    num = int(input())
    print("YES" if isprime(sumOfElement(num)) else "NO")