# https://leetcode.com/problems/range-sum-query-2d-mutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.mat = matrix
        self.grid = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                self.grid[i][j] = matrix[i][j] + self.grid[i+1][j] + self.grid[i][j+1] - self.grid[i+1][j+1]
        self.dic = collections.defaultdict(int)
        
    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.mat[row][col]
        self.mat[row][col] = val
        m, n = len(self.mat), len(self.mat[0])
        for i in range(row+1):
            for j in range(col+1):
                self.grid[i][j] += diff
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row1][col1] - self.grid[row1][col2+1] - self.grid[row2+1][col1] + self.grid[row2+1][col2+1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)