def sumdigit(a):
    s = 0
    while a > 0:
        s += a % 10
        a//=10
    return s

test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    numbers = [int(i) for i in input().split()]
    print(*sorted(numbers, key=lambda item: (sumdigit(item), item)))