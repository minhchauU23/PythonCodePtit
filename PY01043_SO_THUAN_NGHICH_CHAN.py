import queue


def geneEvenPalindrome():
    table = []
    queue = [2, 4, 6, 8]
    while len(queue) > 0:
        num = queue.pop(0)
        table.append(int(str(num) + str(num)[::-1]))
        for i in range(0, 9, 2):
            if num *10 +  i < 1000:
                queue.append(num*10 + i)
    return table

table = geneEvenPalindrome()
test = int(input())
while test > 0:
    test -=1
    num = int(input())
    for item in table:
        if item < num:
            print(item, end = " ")
    print()