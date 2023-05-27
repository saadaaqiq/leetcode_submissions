# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    par = [i for i in range(n)]
    rank = [0] * n

    def find(i):
      if par[i] != i:
        par[i] = find(par[i])
      return par[i]
    
    def union(i, j):
      x, y = find(i), find(j)
      if rank[x] >= rank[y]:
        par[y] = x
        rank[x] += 1 if rank[x]==rank[y] else 0
      else:
        par[x] = y
    
    for a,b in edges:
      union(a, b)
    
    for i in range(n):
      find(i)

    return len(set(par))