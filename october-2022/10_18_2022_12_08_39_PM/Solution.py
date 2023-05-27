# https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
    res = 0
    
    def man(i,j):
      return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
    
    edges = []
    for i in range(len(points)-1):
      for j in range(i+1, len(points)):
        edges.append((i, j, man(i,j)))
        
    edges.sort(key=lambda x:x[2])
    
    parent = [i for i in range(len(points))]
    rank = [0 for i in range(len(points))]
    
    def find(i):
      if parent[i] != i:
        parent[i] = find(parent[i])
      return parent[i]
    
    def union(i,j):
      if rank[i] > rank[j]:
        parent[j] = i
      elif rank[j] > rank[i]:
        parent[i] = j
      else:
        parent[j] = i
        rank[i] += 1
        
    i, k = 0, 0
    
    while k < len(points)-1:
      p1, p2, cost = edges[i]
      i += 1
      x, y = find(p1), find(p2)
      if x != y:
        k += 1
        res += cost
        union(x, y)
    
    return res
      
      
      
      
      
      
      
      
      
    
    
        
    