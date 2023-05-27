# https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        left = [[0] * (n+1) for i in range(m)]
        for i in range(m):
            for j in range(n):
                left[i][j+1] = left[i][j] + matrix[i][j]
        up = [[0] * n for i in range(m+1)]
        for j in range(n):
            for i in range(m):
                up[i+1][j] = up[i][j] + matrix[i][j]
        self.accum = [[0] * (n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.accum[i][j] = matrix[i][j] + self.accum[i-1][j-1] + left[i][j] + up[i][j]
        for row in self.accum:
            print(row)

    def sumRegion(self, up: int, left: int, bottom: int, right: int) -> int:

        a = self.accum[bottom][right]
        
        x = self.accum[up-1][right]
        y = self.accum[bottom][left-1]
        z = self.accum[up-1][left-1]

        return a - x - y + z
