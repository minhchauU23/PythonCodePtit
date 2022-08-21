
def printNumber(a, k, n):
    if a >= n or k == 0:
        print(-1)
        return
    start = a + k - (a % k)
    if start > n:
        print(-1)
        return
    for b in range(start, n + 1, k):
        print(b - a, end = ' ')
    print()

def Test():
    a, k, n = [int(i) for i in input().split()]
    printNumber(a, k, n)

Test()