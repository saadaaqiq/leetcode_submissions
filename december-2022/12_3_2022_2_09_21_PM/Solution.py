# https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*(n-2) for _ in range(m-2)]
        def dir(i,j):
            return [(i-1,j-1), (i-1,j), (i-1,j+1), (i, j-1), (i,j), (i,j+1), (i+1,j-1),(i+1,j),(i+1,j+1)]
        for i in range(1,m-1):
            for j in range(1,n-1):
                res[i-1][j-1] = max([grid[r][c] for (r,c) in dir(i,j)])
        return res