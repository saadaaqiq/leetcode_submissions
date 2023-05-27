# https://leetcode.com/problems/number-of-distinct-islands

class Solution:
  def numDistinctIslands(self, grid: List[List[int]]) -> int:
    parent = {}
    rank = {}
    m, n = len(grid), len(grid[0])
    vis = set()

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          parent[(i,j)] = (i,j)
          rank[(i,j)] = 0
        
    def find(c):
      if parent[c] != c:
        parent[c] = find(parent[c])
      return parent[c]
      
    def union(c1, c2):
      p1, p2 = find(c1), find(c2)
      if rank[p1] > rank[p2]:
        parent[p2] = p1
      elif rank[p1] < rank[p2]:
        parent[p1] = p2
      else:
        parent[p2] = p1
        rank[p1] += 1
    
    def dfs(i,j,pi,pj):
      if (i,j) not in vis and grid[i][j] == 1:
        vis.add((i,j))
        if pi != -1:
          union((i,j), (pi,pj))
        if i < len(grid)-1:
          dfs(i+1, j, i, j)
        if i > 0:
          dfs(i-1, j, i, j)
        if j < len(grid[0])-1:
          dfs(i, j+1, i, j)
        if j > 0:
          dfs(i, j-1, i, j)
      
    for i in range(m):
      for j in range(n):
        dfs(i,j,-1,-1)
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          find((i,j))
          
    dic = {}
    for c in parent:
      if parent[c] not in dic:
        dic[parent[c]] = []
      dic[parent[c]].append(c)
      
    res = len(dic)
    
    myvis = set()
        
    for c1 in dic:
      if c1 in myvis:
        continue
      for c2 in dic:
        if c2 in myvis:
          continue
        if c1 != c2 and len(dic[c1]) == len(dic[c2]):
          if len(set([(dic[c1][i][0]-dic[c2][i][0], dic[c1][i][1]-dic[c2][i][1]) for i in range(len(dic[c1]))])) == 1:
            myvis.add(c2)
            res -= 1
      myvis.add(c1)
    
    return res
            
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
        