# https://leetcode.com/problems/redundant-connection

class Solution:
  
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
    ranks = [ 1 ] * (len(edges)+1)
    parents = [ i for i in range(len(edges)+1) ]
    
    def find(i):
      p = parents[i]
      while p != parents[p]:
        parents[p] = parents[parents[p]]
        p = parents[p]
      return p
    
    def union(i,j):
      p, q = find(i), find(j)
      if p == q:
        return False
      if ranks[p] > ranks[q]:
        parents[q] = p
        ranks[p] += 1
      else:
        parents[p] = q
        ranks[q] += 1
      return True
    
    for edge in edges:
      if not union(edge[0], edge[1]):
        return edge
        
    