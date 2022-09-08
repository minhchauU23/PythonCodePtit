from math import isqrt


def checkAndAddIndex(num, start):
    sum = 0
    for i in range(start, len(num), 2):
        if int(num[i]) % 2 != start: return -1
        sum += int(num[i])
    return sum

def isPrime(num):
    if num == 2: 
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, isqrt(num), 2):
        if num % i == 0: return False
    return True

def resolve(num):
    s1 = checkAndAddIndex(num, 0)
    if s1 == -1: return False
    s2 = checkAndAddIndex(num, 1)
    if s2 == -1: return False
    return isPrime(s1 + s2)

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print("YES" if resolve(num) else "NO")


