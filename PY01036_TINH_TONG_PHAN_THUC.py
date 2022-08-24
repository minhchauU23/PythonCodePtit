


def sum(num):
    res = 0.0
    if num % 2 == 0:
        for i in range(2, num + 1, 2):
            res += 1/i
    else:
         for i in range(1, num + 1, 2):
            res += 1/i
    return res


def Test():
    test = int(input())
    while test > 0:
        test -= 1
        num = int(input())
        print("%.6f" %sum(num))
Test()