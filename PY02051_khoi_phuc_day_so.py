
size = int(input())
grid = []
for i in range(size):
    grid.append([int(j) for j in input().split()])
if size == 2:
    print(grid[0][1]//2, grid[0][1]//2, sep= " ")
else:
    ak = (grid[size - 3][size - 2] + grid[size - 3][size - 1] - grid[size - 2][size - 1]) // 2
    k = size - 3
    result = [0 for i in range(size)]
    if k != 0:
        result[0] = grid[0][k] - ak
    else:
        result[0] = ak
    for i in range(1, size):
        result[i] = grid[0][i] - result[0]
    print(*result)


# 4
# 0 3 6 7
# 3 0 5 6
# 6 5 0 9
# 7 6 9 0
