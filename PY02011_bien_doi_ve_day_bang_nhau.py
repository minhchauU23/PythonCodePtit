
size = int(input())
arr = [int(i) for i in input().split()]
countStep = [0 for i in range(size)]

for i in range(size):
    for j in range(size):
        if i != j:
            countStep[i] += abs(arr[i] - arr[j])

mnStep = min(countStep)
for i in range(size):
    if countStep[i] == mnStep:
        print(countStep[i], arr[i], sep=' ')
        break
