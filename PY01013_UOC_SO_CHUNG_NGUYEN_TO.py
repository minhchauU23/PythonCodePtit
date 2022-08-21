
import math


def isPrime(num):
    if num == 2: return True
    if num < 2 or num % 2 == 0: return False
    for nb in range(3, int(math.sqrt(num)), 2):
        if num % nb == 0: return False
    return True

def sumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    return sum

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        a, b = [int(i) for i in input().split()]
        sumdigit = sumOfDigits(math.gcd(a, b))
        print("YES" if isPrime(sumdigit) else "NO")
Test()