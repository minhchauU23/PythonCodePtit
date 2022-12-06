def DFS(start, end, adj, visited):
    if start == end:
        return True
    for u in adj[start]:
        if visited[u] == False:
            visited[u] = True
            if DFS(u, end, adj, visited):
                return True
    return False

test = int(input())
while test > 0:
    test -= 1
    N, M, u, v = [int(i) for i in input().split()]
    adj = [[] for i in range(N + 1)]
    for e in range(M):
        edg = [int(i) for i in input().split()]
        adj[edg[0]].append(edg[1])
    cnt = 0
    for x in range(1, N + 1):
        if x != u and x!= v:
            visited = [False for i in range(N + 1)]
            visited[u] = True
            visited[x] = True
            if DFS(u, v, adj, visited) == False:
                cnt += 1
    print(cnt)
# 2
# 5 7 1 3
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4