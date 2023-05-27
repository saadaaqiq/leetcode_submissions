# https://leetcode.com/problems/maximal-square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        grid = [[0]*n for i in range(m)]
        res = 0
        for j in range(n):
            grid[m-1][j] = int(matrix[m-1][j])
            res = max(res, grid[m-1][j])
        for i in range(m):
            grid[i][n-1] = int(matrix[i][n-1])
            res = max(res, grid[i][n-1])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] = 0 if matrix[i][j]=="0" else (1 + (min(grid[i+1][j+1] if i+1<m and j+1<n else math.inf, grid[i+1][j] if i+1<m else math.inf, grid[i][j+1] if j+1<n else math.inf) if i+1<m or j+1<n else 0))
                res = max(res, grid[i][j])
        return res * res


        # 0 1
        # 1 0
