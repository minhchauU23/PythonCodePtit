

test = int(input())
while test > 0:
    test-=1
    s = int(input())
    num = 0
    while s > 0:
        num += s%10
        s//=10
    if num > 10 and str(num) == str(num)[::-1] :
        print("YES")
    else: print("NO")

