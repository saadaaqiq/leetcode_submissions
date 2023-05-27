# https://leetcode.com/problems/number-of-closed-islands

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            grid[i][j] = 2
            for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0<=i+dy<m and 0<=j+dx<n and grid[i+dy][j+dx]==0:
                    dfs(i+dy,j+dx)
            
        for i in range(m):
            for j in [0,n-1]:
                if grid[i][j]==0:
                    dfs(i,j)
        for i in [0,m-1]:
            for j in range(n):
                if grid[i][j]==0:
                    dfs(i,j)
        
        def func(i,j):
            grid[i][j] = 3
            for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0<=i+dy<m and 0<=j+dx<n and grid[i+dy][j+dx]==0:
                    func(i+dy,j+dx)
        
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    func(i,j)
        
        return res