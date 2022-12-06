def DFS(start, adj, visited):
    visited[start] = True
    for v in adj[start]:
        if visited[v] == False:
            DFS(v, adj, visited)

N, M, X = [int(i) for i in input().split()]
adj = [[] for v in range(N+1)]
for e in range(M):
    edg = [int(v) for v in input().split()]
    adj[edg[0]].append(edg[1])
    adj[edg[1]].append(edg[0])
visited = [False for v in range(N + 1)]
DFS(X, adj, visited)
ok = False
for i in range(1, N + 1):
    if visited[i] == False:
        print(i)
        ok = True
if not ok:
    print(0)