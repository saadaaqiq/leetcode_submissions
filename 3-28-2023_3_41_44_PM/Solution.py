# https://leetcode.com/problems/minimum-path-sum

from collections import deque
from math import inf

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mat = [[inf] * n for i in range(m)] 
        mat[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                for r, c in [(i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n:
                        mat[i][j] = min(mat[i][j], grid[i][j] + mat[r][c])
        

        return mat[m-1][n-1]
            

