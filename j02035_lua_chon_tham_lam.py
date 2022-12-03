def getMax(n, s):
    if n*9 < s or (s == 0 and n > 1 ):
        return -1
    res = ''
    nb9 = s//9
    s -= nb9*9
    for i in range(nb9):
        res += '9'
    while len(res) < n:
        res += str(s)
        s -= s
    return res

def getMin(n, s):
    if n*9 < s or (s == 0 and n > 1 ):
        return -1
    if s == 0 and n == 1: return 0;
    res = ''
    s-=1
    nb9 = s//9
    s -= nb9*9
    for i in range(nb9):
        res += '9'
    while len(res) < n:
        res = str(s) + res
        s -= s
    res = str(int(res[0]) + 1) + res[1:]
    return res


n, s = [int(i) for i in input().split()]
print(getMin(n,s), getMax(n, s), sep= " ")