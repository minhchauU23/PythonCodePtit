
test = int(input())
while test > 0:
    test -= 1
    N, M, L = [int(i) for i in input().split()]
    grid = [[0 for i in range(M + 1)] for j in range(N + 1)]
    for i in range(1, N+ 1):
        row = [int(x) for x in input().split()]
        for j in range(M):
            grid[i][j + 1] = row[j] + grid[i-1][j + 1] + grid[i][j] - grid[i-1][j]
    for i in range(L, N+1):
        for j in range(L, M+1):
            print((grid[i][j] - grid[i-L][j] - grid[i][j-L] + grid[i-L][j-L])//(L**2), end= " ")
        print()



# 2
# 4 4 3
# 2 1 0 0
# 3 2 1 1
# 4 5 2 1
# 2 2 9 0
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9