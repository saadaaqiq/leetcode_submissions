# https://leetcode.com/problems/connecting-cities-with-minimum-cost

class Solution:
  def minimumCost(self, n: int, connections: List[List[int]]) -> int:
    
    total_cost   = 0
    parent       = [i   for i in range(n+1)]
    rank         = [0   for i in range(n+1)]
    
    connections.sort(key=lambda x:x[2])
    
    def find(x):
      if parent[x] != x: parent[x] = find(parent[x])
      return parent[x]
    
    def union(x, y):
      if rank[x] < rank[y]: parent[x] = y
      elif rank[x] > rank[y]: parent[y] = x
      else: parent[y], rank[x] = x, rank[x] + 1
    
    i, k = 0, 0
    while k < n-1:
      x, y = find(connections[i][0]), find(connections[i][1])
      i += 1
      if x != y:
        k += 1
        union(x, y)
        total_cost += connections[i-1][2]
      if i == len(connections): break
    
    for j in range(1,n+1): find(j)
    
    return total_cost if len(set(parent[1:])) == 1 else -1