from math import isqrt

prime = [2, 3, 5, 7]

def isPrime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, isqrt(num), 2):
        if num % i == 0: return False
    return True

def countPrime(num):
    cnt = 0
    for i in range(len(num)):
        val = int(num[i])
        if val in prime: 
            cnt += 1
    return cnt

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    x = countPrime(num)
    print("YES" if isPrime(len(num)) and  x> (len(num) - x) else "NO")