from audioop import mul


def mulOfOddIndex(num):
    allZero = True
    mult  = 1
    for i in range(1, len(num), 2):
        if int(num[i]) != 0:
            mult *= int(num[i])
            allZero = False
    if allZero: return 0
    return mult

def sumOfEvenIndex(num):
    sum = 0
    for i in range(0, len(num), 2):
        sum += int(num[i])
    return sum

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print(sumOfEvenIndex(num), mulOfOddIndex(num), sep= " ")