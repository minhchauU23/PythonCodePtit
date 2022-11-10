

from itertools import combinations
from math import gcd



nb = int(input())
arr = [int(i) for i in input().split()]
for pr in combinations(sorted(arr), 2):
    if gcd(pr[0], pr[1]) == 1:
        print(*pr)
        
