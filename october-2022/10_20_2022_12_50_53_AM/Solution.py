# https://leetcode.com/problems/minimize-maximum-value-in-a-grid

class Solution:
  def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    res = [[0 for j in range(n)] for i in range(m)]
    adj = {}
    starters = set()
    for i in range(m):
      for j in range(n):
        adj[(i,j)] = []
    for i in range(m):
      l = sorted([(grid[i][j], (i,j)) for j in range(n)], reverse = True)
      starters.add(l[0][1])
      for k in range(n-1):
        adj[l[k][1]].append(l[k+1][1])
    for j in range(n):
      l = sorted([(grid[i][j], (i,j)) for i in range(m)], reverse = True)
      starters.add(l[0][1])
      for k in range(m-1):
        adj[l[k][1]].append(l[k+1][1])
    
    def dfs(i,j):
      if res[i][j] == 0:
        res[i][j] = 1 if not adj[(i,j)] else 1 + max([dfs(c[0],c[1]) for c in adj[(i,j)]])
        if not adj[(i,j)]:
          res[i][j] = 1
        else:
          m = 0
          for c in adj[(i,j)]:
            m = max(m, dfs(c[0], c[1]))
          res[i][j] = 1 + m
      return res[i][j]
    
    for cell in starters:
      dfs(cell[0], cell[1])
      
    return res
    
        