
s = str(input())
limit = int(input())
res = dict()
for i in range(0, len(s), 2):
    x = int(s[i:min(i+2, len(s))])
    if x <= 9 : continue
    if res.get(x) is None:
        res.update({x: 1})
    else:
        res[x] += 1

ok = False
for x in sorted(res):
    if res.get(x) >= limit:
        ok = True
        print(x, res.get(x), sep= " ")
if ok == False:
    print("NOT FOUND")