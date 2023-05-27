# https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mat = [[0 for j in range(n)] for i in range(m)]
        down, right = -1, -1
        for i in range(m-1, -1, -1):
            if grid[i][n-1] == 1:
                right = i
                break
        for i in range(m-1, -1, -1):    
            mat[i][n-1] = 1 if i > right else 0
        for j in range(n-1, -1, -1):
            if grid[m-1][j] == 1:
                down = j
                break
        for j in range(n-1):
            mat[m-1][j] = 1 if j > down else 0
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if grid[i][j] != 1:
                    mat[i][j] += mat[i+1][j] + mat[i][j+1]
        return mat[0][0]