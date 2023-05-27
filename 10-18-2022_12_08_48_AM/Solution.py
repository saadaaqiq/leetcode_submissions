# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
    res = 0
    
    edges = []
    for i in range(len(points)-1):
      for j in range(i+1, len(points)):
        edges.append((i, j, abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])))
    edges.sort(key=lambda x:x[2])
    
    parent = [i for i in range(len(points))]
    rank = [0 for i in range(len(points))]
    
    def find(x):
      if parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]
    
    def union(x, y):
      if rank[x] < rank[y]:
        parent[x] = y
      elif rank[y] < rank[x]:
        parent[y] = x
      else:
        parent[y] = x
        rank[x] += 1
    
    i, k = 0, 0
    
    while k < len(points)-1:
      p1, p2, w = edges[i]
      i += 1
      x = find(p1)
      y = find(p2)
      if x != y:
        k += 1
        res += w
        union(x, y)
        
    return res
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
    
    
        
    