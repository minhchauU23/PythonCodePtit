from itertools import permutations

test = int(input())
while test > 0:
    test -= 1
    sz = int(input())
    permutation = list(permutations([int(i) for i in range(sz, 0, -1)]))
    print(len(permutation))
    for x in permutation:
        print(*x, sep="", end= " ")
    print()
