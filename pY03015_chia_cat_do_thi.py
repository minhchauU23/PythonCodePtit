def DFS(u, adj, visited):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            DFS(v, adj, visited)

def countConnected(adj, u,  N):
    cntConnect = 0
    visited = [False for i in range(N + 1)]
    visited[u] = True
    for v in range(1, N + 1):
        if visited[v] == False:
            DFS(v, adj, visited)
            cntConnect += 1
    return cntConnect

test = int(input())
while test > 0:
    test -= 1
    N, M = [int(i) for i in input().split()]
    adj = [[] for i in range(N + 1)]
    for e in range(M):
        edg = [int(i) for i in input().split()]
        adj[edg[0]].append(edg[1])
        adj[edg[1]].append(edg[0])
    mxConnect = countConnected(adj, 0, N)
    u = 0
    for i in range(1, N + 1):
        cnt = countConnected(adj, i, N)
        if cnt > mxConnect:
            u = i
            mxConnect = cnt
    print(u)