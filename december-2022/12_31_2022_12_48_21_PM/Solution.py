# https://leetcode.com/problems/unique-paths-iii

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, o, si, sj, res, vis= len(grid), len(grid[0]), 0, 0, 0, 0, set()
        free = m*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1: 
                    free -= 1
                elif grid[i][j] == 1: 
                    si, sj = i, j

        def dfs(i,j,s):
            nonlocal res, m, n, free
            if grid[i][j] == 2 and s==free:
                
                res += 1
            else:
                vis.add((i,j))
                for (r,c) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and (r,c) not in vis and grid[r][c] != -1:
                        dfs(r,c,s+1)
                vis.remove((i,j))

        dfs(si,sj,1)
        return res
        
            
