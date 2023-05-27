# https://leetcode.com/problems/unique-paths-iii

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, obst, si, sj, res, vis = len(grid), len(grid[0]), 0, 0, 0, 0, set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: si, sj = i, j
                if grid[i][j] == -1: obst += 1
        
        def dfs(i,j,steps):
            nonlocal res, m, n, obst
            if grid[i][j] == 2 and steps + 1 == m*n - obst:
                res += 1
            else:
                vis.add((i,j))
                for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c] != -1 and (r,c) not in vis:
                        dfs(r,c,steps+1)
                vis.remove((i,j))

        dfs(si, sj, 0)

        return res




