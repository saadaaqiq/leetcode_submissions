# https://leetcode.com/problems/max-area-of-island

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    vis = set()
    m,n = len(grid), len(grid[0])
    maxi = 0
    def dfs(i,j):
      if i<0 or i==m or j<0 or j==n or (i,j) in vis or grid[i][j]==0:
        return 0 
      vis.add((i,j))
      return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
    
    for i in range(m):
      for j in range(n):
        if grid[i][j]!=0 and (i,j) not in vis:
          maxi = max(maxi, dfs(i,j))
    
    return maxi