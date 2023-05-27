# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
    parents = [ i for i in range(n) ]
    
    ranks = [ 1 ] * n
    
    def find(i):
      p = parents[i]
      while parents[p] != p:
        parents[p] = parents[parents[p]]
        p = parents[p]
      return p
      
    def union(i,j):
      p, q = find(i), find(j)
      if p == q:
        return False
      if ranks[p] > ranks[q]:
        parents[q] = p
        for k in range(n):
          if parents[k] == q:
            parents[k] = p
        ranks[p] += 1
      else:
        parents[p] = q
        for k in range(n):
          if parents[k] == p:
            parents[k] = q
        ranks[q] += 1
      return True
    
    for i,j in edges:
      union(i,j)
      
    return len(set(parents))