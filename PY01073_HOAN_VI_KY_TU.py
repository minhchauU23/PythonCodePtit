from itertools import permutations


s = str(input())
for item in permutations(s):
    print(*item, sep = '')
