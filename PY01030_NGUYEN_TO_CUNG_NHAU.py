
import math


n, k = [int(i) for i in input().split(' ')]
cnt = 0
for i in range(10**(k-1), 10**(k)):
    if math.gcd(i, n)==1 :
        cnt += 1
        print(i, end = ' ')
        if cnt == 10:
            cnt = 0
            print()