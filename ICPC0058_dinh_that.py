adj = []
visited = []
def DFS(src, des):
    if src == des:
        return True
    for x in adj[src]:
        if visited[x] == False:
            visited[x] = True
            if DFS(x, des):
                return True
    return False


test = int(input())
while test > 0:
    test -= 1
    N, M, u, v = [int(i) for i in input().split()]
    adj.clear()
    visited.clear()
    for i in range(N + 1):
        adj.append([])
    for i in range(M):
        edg = [int(i) for i in input().split()]
        adj[edg[0]].append(edg[1])
    cnt = 0
    for i in range(1, N + 1):
        if i != u and i != v:
            for j in range(N + 1):
                visited.append(False)
            visited[u] = True
            visited[i] = True
            if DFS(u, v) == False:
               cnt += 1
            visited.clear()
    print(cnt)
    # print(adj)
# 2
# 5 7 1 3
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4