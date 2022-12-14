from collections import deque


def BFS(grid, visited, n, m):
    step = [[1, 0], [0, 1], [1, 1]]
    dq = deque()
    dq.append([0,0,0])
    visited[0][0] = True
    while len(dq) > 0:
        front = dq.popleft()
        if front[0] == n - 1 and front[1] == m - 1:
            return front[2]
        for index in range(len(step)):
            row = front[0]
            col = front[1]
            s = step[index]
            if row + s[0] < n and col + s[1] < m:
                diff = abs(grid[row][col] - grid[row + s[0]][col + s[1]])
                if index == 0:
                    row += diff
                elif index == 1:
                    col += diff
                else:
                    row += diff
                    col += diff
                if row < n and col < m and visited[row][col] == False:
                    if row == n-1 and col == m -1:
                        return front[2] + 1
                    visited[row][col] = True
                    dq.append([row, col, front[2] + 1])
    return -1

grid = [[0 for i in range(1000)] for j in range(1000)]
visited = [[False for i in range(1000)] for j in range(1000)]
test = int(input())
while test > 0:
    test -= 1
    n,m = [int(i) for i in input().split()]
    for i in range(n):
        line = input().split()
        for j in range(m):
            grid[i][j] = int(line[j])
            visited[i][j] = False
    print(BFS(grid, visited, n, m))

