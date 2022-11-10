
def count(a, id):
    cnt = 0
    for i in range(len(a)):
        if i != id:
            ss = a[i]
            while ss != a[id]:
                cnt += 1
                ss = ss[1:] + ss[0]
                if ss == a[i]: return -1
    return cnt

n = int(input())
a = []
for x in range(n):
    tmp = str(input())
    a.append(tmp)

res = count(a, 0)
if res == -1: print(-1)
else:
    for i in range(1, len(a)):
        cn = count(a, i)
        if cn == -1: print(-1)
        else:
            res = min(res, count(a, i))
    print(res)