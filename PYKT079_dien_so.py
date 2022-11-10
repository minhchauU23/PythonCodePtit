
test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    arr = set([int(i) for i in input().split()])
    print(max(arr) - min(arr) + 1 - len(arr))