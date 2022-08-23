import math


def check(num):
    sum = num[0]
    for i in range(1, len(num)):
        sum += num[i]
        if abs(num[i] - num[i-1]) != 2: return "NO"
    return "YES" if (sum % 10 == 0) else "NO"



def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        num = [int(i) for i in input()]
        print(check(num))
Test()