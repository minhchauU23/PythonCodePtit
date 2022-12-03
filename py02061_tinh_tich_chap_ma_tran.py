def convolution(matrix, kernel):
    s = 0
    for i in range(0, len(matrix) - len(kernel) + 1):
        newRow = []
        for j in range(0, len(matrix[0]) - len(kernel[0]) + 1):
            tmp = []
            tmp.append(matrix[i][j:j+3])
            tmp.append(matrix[i+1][j:j+3])
            tmp.append(matrix[i+2][j: j + 3])
            newRow.append(mul(tmp, kernel))
        s += sum(newRow)
    return s
def mul(firstMatrix, secondMatrix):
    result = 0
    for i in range(3):
        for j in range(3):
            result += firstMatrix[i][j] * secondMatrix[i][j]
    return result



test = int(input())
while test > 0:
    test -= 1
    row, column = [int(i) for i in input().split()]
    matrix = []
    kernel = []
    for i in range(row):
        valRow = [int(i) for i in input().split()]
        matrix.append(valRow)
    for i in range(3):
        valRow = [int(i) for i in input().split()]
        kernel.append(valRow)
    print(convolution(matrix, kernel))
# 2
# 4 4
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 1 1 1
# 1 1 1
# 1 1 1