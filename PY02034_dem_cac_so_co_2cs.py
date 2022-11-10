
s = input()
res = dict()
for i in range(0, len(s), 2):
    x = int(s[i:min(i+2, len(s))])
    if x <= 9 : continue
    if res.get(x) is None:
        res.update({x: 1})
    else:
        res[x] += 1
for k in res:
    print(k, res[k], sep=' ')