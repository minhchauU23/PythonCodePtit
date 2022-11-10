def check(arr1, arr2, size):
    for i in range(0, size):
        if arr1[i] > arr2[i]: return False
    return True

test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    print("YES" if check(sorted(arr1), sorted(arr2), size) else "NO")