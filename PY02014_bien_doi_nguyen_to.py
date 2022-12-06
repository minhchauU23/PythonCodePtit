prime = [True for i in range(10001)]
prime[0] = prime[1] = False
countStep = [10000 for i in range(10001)]
def erathone():
    countStep[0] = 2
    countStep[1] = 1
    preIndex = 2
    for i in range(2, 10001, 1):
        if prime[i] == True:
            countStep[i] = 0
            for j in range(i * i, 10001, i):
                prime[j] = False
            for j in range(preIndex + 1, i):
                if j - preIndex <= i - j:
                    countStep[j] = j - preIndex
                else:
                    countStep[j] = i - j
            preIndex = i

erathone()
size = int(input())
arr = [int(i) for i in input().split()]
minStep = countStep[arr[0]]
for i in range(1, len(arr)):
    minStep = max(countStep[arr[i]], minStep)
print(minStep)
# 8
# 13 5 8 7 9 15 26 34