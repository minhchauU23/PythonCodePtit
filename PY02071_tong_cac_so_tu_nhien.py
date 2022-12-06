result = []
def backTrack(arr, index, maxVal, currentSum, sum):
    for val in range(maxVal, 0, -1):
        if currentSum + val <= sum:
            arr[index] = val
            if currentSum + val == sum:
                result.append(arr[1:index + 1])
            backTrack(arr, index + 1, arr[index], currentSum + val, sum)


test = int(input())
while test > 0:
    test -= 1
    result.clear()
    s = int(input())
    arr = [0 for i in range(s + 1)]
    backTrack(arr, 1, s, 0, s)
    print(len(result))
    for ai in result:
        print("(", end="")
        print(*ai, end="")
        print(")", end= " ")
    print()