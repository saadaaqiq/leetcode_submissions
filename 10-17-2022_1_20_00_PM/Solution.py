# https://leetcode.com/problems/find-if-path-exists-in-graph

class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    parents = [i for i in range(n)]
    ranks = [1 for i in range(n)]
    
    def union(x, y):
      px, py = x, y
      while parents[px] != px: px = parents[px]
      while parents[py] != py: py = parents[py]
      if ranks[px] > ranks[py] or (ranks[px] == ranks[py] and x < y):
        parents[y] = px
        ranks[px] += 1
      elif ranks[px] < ranks[py] or (ranks[px] == ranks[py] and x > y):
        parents[x] = py
        ranks[py] += 1
      
    def find(x):
      px = x
      while parents[px] != px: px = parents[px]
      return px
      
    for x, y in edges:
      union(x, y)
      
    return find(source) == find(destination)