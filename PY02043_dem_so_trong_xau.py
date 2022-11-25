def countNB(s, nb):
    cnt = 0
    while nb in s:
        cnt += 1
        s = s[s.find(nb) + len(nb) ::]
    return cnt


test = int(input())
while test > 0:
    test -= 1
    nb = str(input())
    nf = str(input())
    print(countNB(nb, nf))
