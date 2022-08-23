import math

def convert(num):
    if len(num) <= 3: return num
    sz = -len(num) - int((len(num) - 1)/3) - 1
    for i in range(-4, sz, -4):
        num = num[:i + 1] + "," + num[i + 1:]
        i -= 1
    return num

def Test():
    # numOfTest = int(input())
    # for test in range(numOfTest):
        num = str(input())
        print(convert(num))
Test()