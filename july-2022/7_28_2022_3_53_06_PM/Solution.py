# https://leetcode.com/problems/graph-valid-tree

class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    ranks = [ 1 ] * n
    parents = [ i for i in range(n) ]
    
    def find(i):
      p = parents[i]
      while p != parents[p]:
        parents[p] = parents[parents[p]]
        p = parents[p]
      return p
    
    def union(i,j):
      p, q = find(i), find(j)
      if p == q:
        return 0
      if ranks[p] > ranks[q]:
        parents[q] = p
        ranks[p] += 1
      else:
        parents[p] = q
        ranks[q] += 1
      return 1
    
    conn = n
    for edge in edges:
      if union(edge[0], edge[1]) == 0:
        return False
      conn -= 1 
        
    return conn == 1
        
    