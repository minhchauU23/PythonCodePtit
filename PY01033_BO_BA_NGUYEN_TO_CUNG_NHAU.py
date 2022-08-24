

import math


def listed(l, r):
    for i in range(l, r):
        for j in range(i+1, r):
            if math.gcd(i, j) == 1:
                for k in range(j + 1, r):
                    if math.gcd(i,k) == 1 and math.gcd(j, k) == 1:
                        print("({0}, {1}, {2})".format( i, j, k))



l, r = [int(i) for i in input().split(' ')]
listed(l, r + 1)