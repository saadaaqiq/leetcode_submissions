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
                if i == 0 and j == 0:
                    continue
                mat[i][j] = grid[i][j] + min(mat[i-1][j] if i>0 else inf, mat[i][j-1] if j>0 else inf)
        return mat[m-1][n-1]
            

