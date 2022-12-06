
nbOfVertex = int(input())
adj = [0 for i in range(nbOfVertex + 1)]
for i in range(nbOfVertex - 1):
    edg = [int(v) for v in input().split()]
    adj[edg[0]] += 1
    adj[edg[1]] += 1
ok = False
for i in range(1, nbOfVertex + 1):
    if adj[i] == 1:
        continue
    elif adj[i] == nbOfVertex - 1 and ok == False:
        ok = True
    else:
        ok = False
        break
print("Yes" if ok else "No")