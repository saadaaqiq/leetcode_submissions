# https://leetcode.com/problems/minimize-maximum-value-in-a-grid

class Solution:
  def minScore(self, grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    res, adj = [[0 for j in range(n)] for i in range(m)], {}
    starters, heap = [], []

    for i in range(m):
      for j in range(n):
        adj[(i,j)] = []

    for i in range(m):
      for j in range(n):
        heapq.heappush(heap, (-grid[i][j], (i,j)))      
      starters.append(heapq.heappop(heap)[1])
      old = starters[-1]
      while heap:
        adj[old].append(heapq.heappop(heap)[1])
        old = adj[old][-1]
        
    for j in range(n):
      for i in range(m):
        heapq.heappush(heap, (-grid[i][j], (i,j)))
      starters.append(heapq.heappop(heap)[1])
      old = starters[-1]
      while heap:
        adj[old].append(heapq.heappop(heap)[1])
        old = adj[old][-1]
      
    def dfs(i,j):
      if res[i][j] == 0:
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
    
        