import math


class MaTran:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def chuyenVi(self):
        res = []
        for i in range(self.m):
            tmp = []
            for j in range(self.n):
                tmp.append(self.a[j][i])
            res.append(tmp)
        return res

    def inMaTran(self):
        other = self.chuyenVi()
        res = [[0 for i in range(self.n)] for j in range( self.n)]
        for i in range(self.n):
            for j in range(self.n):
                res[i][j] = 0
                for k in range(self.m):
                    res[i][j] += self.a[i][k] * other[k][j]
                    print(res)
                # print(res[i][j], end=" ")
            print(res)
        print(res)


def TC():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    res = MaTran(n, m, a)
    res.inMaTran()


t = 1
t = int(input())
for i in range(t): TC()

# 1
# 2  2
# 1  2
# 3  4