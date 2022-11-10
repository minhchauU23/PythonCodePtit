
test = int(input())
while test > 0:
    test -= 1
    amount = int(input())
    table = [0 for i in range(1001)]
    index = 0
    for i in range(amount):
        k = int(input())
        table[k] += 1
        if table[index] < table[k]: index = k
        elif table[index] == table[k]: index = min(index, k)
    print(index)