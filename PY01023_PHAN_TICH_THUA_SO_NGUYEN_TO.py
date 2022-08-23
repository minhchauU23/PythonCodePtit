from cmath import sqrt
import math
from re import L


def factorize(num):
    template = " * {0}^{1}"
    res = "1"
    cnt = 0
    while num % 2 == 0:
        cnt += 1
        num //= 2
    if cnt > 0 : res += template.format(2, cnt)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        ct = 0
        while num % i == 0 :
            num//= i
            ct += 1
        if ct > 0 : res += template.format(i, ct)
    if num > 1 : res += template.format(num, 1)
    return res

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        s = int(input())
        print(factorize(s))
Test()