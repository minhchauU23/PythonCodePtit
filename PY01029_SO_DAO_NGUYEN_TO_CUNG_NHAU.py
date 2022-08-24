

from cmath import sqrt
import math


def check(num):
    revNum = int(num[::-1])
    num = int(num)
    return math.gcd(num, revNum) == 1

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        num = str(input())
        print("YES" if check(num) else "NO")
Test()
