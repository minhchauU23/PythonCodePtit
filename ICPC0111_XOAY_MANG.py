



test = int(input())
while test > 0:
    test -= 1
    size, k = [int(i) for i in input().split(" ")]
    arr = []
    while len(arr) < size:
        for  i in input().split(" "):
            arr.append(i)
    for i in range(k%size, size):
        print(arr[i], end = " ")
    for i in range(0, k%size):
        print(arr[i], end = " ")
    print()