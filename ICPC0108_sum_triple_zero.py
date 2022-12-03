def sumTripleZero(arr):
    sTriple = 0
    for index in range(0, len(arr) - 2):
        left = index + 1
        right = len(arr) - 1
        while left < right:
            if arr[index] + arr[left] + arr[right] == 0:
                sTriple += 1
                left += 1
            elif arr[index] + arr[left] + arr[right] < 0:
                left += 1
            else:
                right -= 1
    return sTriple





test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    arr = [int(i) for i in input().split()]
    print(sumTripleZero(sorted(arr)))

# 2
# 5
# 0 -1 2 -3 1
# 5
# 1 -2  1  0  5