sz = int(input())
arr = [int(i) for i in input().split()]
arr = sorted(arr)

print(max(arr[0]*arr[1], arr[-1] * arr[-2], arr[-1] * arr[0] * arr[1], arr[-1] * arr[-2] * arr[-3]))