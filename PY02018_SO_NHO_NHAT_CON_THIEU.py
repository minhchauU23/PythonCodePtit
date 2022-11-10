
n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
x = arr[0]
for i in arr:
    if x != i:
        break
    else: x += 1
print(x)