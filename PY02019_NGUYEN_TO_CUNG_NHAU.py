
from itertools import combinations
from xmlrpc.client import boolean

def gcd(a, b):
    while a != 0:
        if a < b:
            tmp = b
            b = a
            a = tmp
        a = a%b 
    return b

n = int(input())
arr = [int(i) for i in input().split()]

for item in combinations(sorted(arr), 2):
    if gcd(item[0], item[1]) == 1: 
        print(*item)