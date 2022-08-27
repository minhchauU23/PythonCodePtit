



table = [1]
for i in range(1, 10):
    table.append(i * table[i-1])
test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    sum = 0
    for i in range(len(num)):
        sum += table[int(num[i])]
    print("Yes" if sum == int(num) else "No")
