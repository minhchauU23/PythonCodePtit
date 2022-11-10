fibo = [0 for i in range(93)]
fibo[1] = 1
for i in range(2, 93):
    fibo[i] = fibo[i-1] + fibo[i-2]

test = int(input())
while test > 0:
    test -= 1
    a, b = [int(i) for i in input().split(' ')]
    for i in range(a, b + 1):
        print(fibo[i], end = ' ')
    print()