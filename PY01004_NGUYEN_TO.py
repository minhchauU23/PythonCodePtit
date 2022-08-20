
from cmath import sqrt


def GCD(num1, num2):
    while num1 > 0 and num2 > 0:
        if num1 < num2:
            tmp = num1
            num1 = num2
            num2 = tmp
        num1 %= num2
    return max(num1, num2)

def isPrimeNumber(num):
    if num <= 1: return False
    elif num == 2: return True
    elif num%2 == 0: return False
    for nb in range(3, int(sqrt(num)), 2):
        if num%nb == 0: return False
    return True

def check(num):
    cnt = 0
    for item in range(1, num):
        if GCD(item, num) == 1: 
            cnt += 1
    return isPrimeNumber(cnt)


def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        num = int(input())
        print("YES" if check(num) else "NO")

Test()