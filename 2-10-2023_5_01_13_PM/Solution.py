# https://leetcode.com/problems/as-far-from-land-as-possible

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if sum([sum(row) for row in grid]) in [0, m*n]:
            return -1
        res = -1

        mat = [[math.inf]*n for i in range(m)]

        for i in range(m):
            l = -1
            for j in range(n):
                if grid[i][j] == 1:
                    l = j
                elif l >= 0:
                    mat[i][j] = min(mat[i][j], j-l)
            r = n
            for j in range(n-1,-1,-1):
                if grid[i][j] == 1:
                    r = j
                elif r < n:
                    mat[i][j] = min(mat[i][j], r-j)
        for j in range(n):
            u = -1
            for i in range(m):
                if grid[i][j] == 1:
                    u = i
                elif u >= 0:
                    mat[i][j] = min(mat[i][j], i-u)
            b = m
            for i in range(m-1, -1, -1):
                if grid[i][j] == 1:
                    b = i 
                elif b < m:
                    mat[i][j] = min(mat[i][j], b-i)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    l = mat[i][j-1] if j>0 else math.inf 
                    r = mat[i][j+1] if j<n-1 else math.inf 
                    u = mat[i-1][j] if i>0 else math.inf 
                    b = mat[i+1][j] if i<m-1 else math.inf 
                    mat[i][j] = min(mat[i][j], l+1, r+1, u+1, b+1)
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] < 100000:
                    res = max(res, mat[i][j])
        return res



