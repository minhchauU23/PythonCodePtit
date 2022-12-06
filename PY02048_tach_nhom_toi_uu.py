size, k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr = sorted(arr)
group = 1
for i in range(1, size):
    if arr[i-1] + k < arr[i]:
        group += 1
print(group)
# arr = [1, 1, 1, 2, 2, 2, 3, 3, 5, 5]
# print(bisect.bisect_right(arr, 5, 0, len(arr)))
# 7 1
# 2 6 1 7 3 4 9