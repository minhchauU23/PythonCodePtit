sz = int(input())

arr = []
while len(arr) < sz:
    for i in input().split():
        arr.append(int(i))
if arr[-1] == sz:
    print("Excellent!")
else:
    for i in range(1, arr[-1]):
        if i not in arr:
            print(i)