
s = input()
res = []
for i in range(0, len(s), 2):
    x = int(s[i:min(i+2, len(s))])
    if x > 9 and x not in res:
        res.append(x)
print(*res)