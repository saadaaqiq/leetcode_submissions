# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    par = [ k for k in range(n) ]
    rank = [1] * n
    
    def find(k):
      i = k
      while i != par[i]:
        par[i] = par[par[i]]
        i = par[i]
      return i
    
    def union(i,j):
      p,q = find(i), find(j)
      if p == q:
        return 0
      if rank[p]>rank[q]:
        par[q] = p
        rank[p] += rank[q]
      else:
        par[p] = q
        rank[q] += rank[p]
      return 1
    
    res = n
    for i,j in edges:
      res -= union(i,j)
    return res