def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True


test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print("YES" if check(sorted(a), sorted(b)) else "NO")
