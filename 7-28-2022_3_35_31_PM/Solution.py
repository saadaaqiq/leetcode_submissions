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
        return 0
      if ranks[p] > ranks[q]:
        parents[q] = p
        ranks[p] += ranks[q]
      else:
        parents[p] = q
        ranks[q] += ranks[p]
      return 1
    
    result = n
    for i,j in edges:
      result -= union(i,j)
      
    return result