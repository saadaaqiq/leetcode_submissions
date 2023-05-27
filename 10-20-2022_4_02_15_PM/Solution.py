# https://leetcode.com/problems/minimize-maximum-value-in-a-grid

class Solution:
  def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    adj = {}
    starters = set()
    res = [[0 for j in range(n)] for i in range(m)]
    
    for i in range(m):
      for j in range(n):
        adj[(i,j)] = []
    
    for i in range(m):
      l= sorted([(grid[i][j],i,j) for j in range(n)], reverse=True)
      starters.add((l[0][1],l[0][2]))
      for k in range(n-1):
        adj[(l[k][1],l[k][2])].append((l[k+1][1],l[k+1][2]))
    
    for j in range(n):
      l = sorted([(grid[i][j],i,j) for i in range(m)], reverse=True)
      starters.add((l[0][1],l[0][2]))
      for k in range(m-1):
        adj[(l[k][1],l[k][2])].append((l[k+1][1],l[k+1][2]))
        
    def dfs(i,j):
      if res[i][j] == 0:
        if not adj[(i,j)]:
          res[i][j] = 1
        else:
          res[i][j] = 1 + max([dfs(r,c) for r,c in adj[(i,j)]]) 
      return res[i][j]
    
    for i,j in starters:
      dfs(i,j)
      
    return res
      
        
        