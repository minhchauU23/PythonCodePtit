import decimal
from decimal import Decimal
def getMaxAverage(C, D, A):
    cntC = sum(A[0:C])
    cntD = sum(A[C:C+D])
    # result = Decimal(cntC/C + cntD/D).quantize("1.000000", decimal.ROUND_HALF_UP)
    return "%.06f"%(cntC/C + cntD/D)


test = int(input())
while test > 0:
    test -= 1
    N, C, D = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    if C > D:
        tmp = C
        C = D
        D = tmp
    A = sorted(A, key=lambda k: -k)
    print(getMaxAverage(C, D, A))