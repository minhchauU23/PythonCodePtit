class Matrix:
    def __init__(self, row, column, grid):
        self.row = row
        self.column = column
        self.grid = grid
    
    def mul(self, matrix):
        rows = self.row
        column = matrix.column
        result = []
        for i in range(rows):
            newRow = [0 for i in range(column)]
            for j in range(column):
                for k in range(self.column):
                    newRow[j] += self.grid[i][k] * matrix.grid[k][j]
            result.append(newRow)
        return Matrix(rows, column, result)
    
    def reverse(self):
        row = self.column
        column = self.row
        grid = []
        for i in range(row):
            newRow = []
            for j in range(column):
                newRow.append(self.grid[j][i])
            grid.append(newRow)
        return Matrix(row, column, grid)
    
    def __str__(self):
        result = ''
        for i in range(self.row):
            for j in range(self.column):
                result += str(self.grid[i][j]) + ' '
            result += '\n'
        return result.strip()               

test = int(input())
while test > 0:
    test -= 1
    n, m = [int(i) for i in input().split()]
    grid = []
    for i in range(n):
        grid.append( [int(k) for k in input().split()]) 
    mt1 = Matrix(n, m, grid)
    print(mt1.mul(mt1.reverse()))
    
        