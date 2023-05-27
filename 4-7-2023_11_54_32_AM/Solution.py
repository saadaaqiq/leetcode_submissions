# https://leetcode.com/problems/number-of-enclaves

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            for (r,c) in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<r<m-1 and 0<c<n-1 and grid[r][c]==1:
                    grid[r][c]=2
                    dfs(r,c)
        
        for i in range(m):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][n-1]==1:
                dfs(i,n-1)
        for j in range(n):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[m-1][j]==1:
                dfs(m-1,j)

        for i in range(m):
            if grid[i][0]==1:
                grid[i][0]=2
            if grid[i][n-1]==1:
                grid[i][n-1]=2
        for j in range(n):
            if grid[0][j]==1:
                grid[0][j]=2
            if grid[m-1][j]==1:
                grid[m-1][j]=2
        
        return sum([Counter(row)[1] for row in grid])
