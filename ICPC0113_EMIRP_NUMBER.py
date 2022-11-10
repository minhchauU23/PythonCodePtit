table = [True for i in range(1000001)]
result = []
def erathone():
    table[0] = table[1] = False
    for i in range(4, 1000001, 2):
        table[i] = False
    for i in range(3, 1000001, 2):
        if table[i]:
            for j in range(i * i, 1000001, i):
                table[j] = False

def generateListPairPrime():
    for i in range(11, 1000001, 2):
        rev = int((str(i)[::-1]))
        if table[i] and (i != rev) and table[rev]:
            table[i] = False
            table[rev] = False
            result.append([i, rev])


erathone()
generateListPairPrime()
test = int(input())
while test > 0:
    test -= 1
    size = int(input())
    for pr in result:
        if pr[0] >= size :break
        if (pr[0] < size and pr[1] < size):
            print(pr[0], pr[1], sep=' ', end = ' ')
    print()
