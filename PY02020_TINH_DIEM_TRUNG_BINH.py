from turtle import update


n = int(input())
arr =[]
while len(arr) < n:
    x = [float(i) for i in input().split()]
    for i in x:
        arr.append(i)
print(arr)
arr.sort()
amount = 0
sum = 0.0
for i in range(0, len(arr)):
    if (arr[i] != arr[0]) and (arr[i] != arr[- 1]):
        amount += 1
        sum += arr[i]
if amount == 0: amount = 1
print("%.2f" %(sum/amount))