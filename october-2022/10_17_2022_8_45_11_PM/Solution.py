# https://leetcode.com/problems/number-of-islands

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    par = {}
    m, n = len(grid), len(grid[0])
    
    def find(cell):
      if par[cell] != cell:
        par[cell] = find(par[cell])
      return par[cell]
    
    def union(c1, c2):
      if c1 not in par:
        par[c1] = c1
      if c2 not in par:
        par[c2] = c2
      par[find(c1)] = find(c2)
      
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          union((i,j), (i,j))
          if (i+1<m and grid[i+1][j] == "1"):
            union((i+1, j), (i,j))
          if (j+1<n and grid[i][j+1] == "1"):
            union((i, j+1), (i,j))
    
    s = set()
    for i,j in par:
      s.add(find((i,j)))
    
    return len(s)