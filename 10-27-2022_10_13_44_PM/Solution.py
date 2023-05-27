# https://leetcode.com/problems/number-of-distinct-islands

class Solution:
  def numDistinctIslands(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    vis = set()
    
    def dfs(i,j,ref_i,ref_j):
      nonlocal m
      nonlocal n
      if (i,j) in vis or grid[i][j] == 0:
        return ""
      vis.add((i,j))
      cellname = str((i-ref_i,j-ref_j))
      right, down, left, up = "", "", "", ""
      if j < n-1: right += dfs(i,j+1,ref_i,ref_j)
      if i < m-1: down  += dfs(i+1,j,ref_i,ref_j)
      if j > 0:   left  += dfs(i,j-1,ref_i,ref_j)
      if i > 0:   up    += dfs(i-1,j,ref_i,ref_j)
      if right: cellname += right
      if down : cellname += down
      if left : cellname += left
      if up   : cellname += up
      return cellname
    
    cells = set()
    
    for i in range(m):
      for j in range(n):
        cells.add(dfs(i,j,i,j))
    if "" in cells:
      cells.remove("")
    
    return len(cells)