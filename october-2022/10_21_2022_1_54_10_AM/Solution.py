# https://leetcode.com/problems/minimize-maximum-value-in-a-grid

class Solution:
  def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    m,n = len(grid),len(grid[0])
    arr = sorted([(grid[i][j],i,j) for i in range(m) for j in range(n)])
    rm, cm = [0 for i in range(m)], [0 for j in range(n)]
    for v, i, j in arr:
      m = max(rm[i], cm[j]) + 1
      rm[i], cm[j] = m, m
      grid[i][j] = m
    return grid