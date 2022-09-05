
test = int(input())
while test > 0:
    test -= 1
    num = int(input())
    mul = 1
    while num > 0:
        if num %10 == 0: 
            num//=10
            continue
        mul *= num%10
        num //= 10
    print(mul)