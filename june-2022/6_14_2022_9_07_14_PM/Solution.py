# https://leetcode.com/problems/network-delay-time

class Solution:
  
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
    edges = { i : [] for i in range(n) }
    start = k-1
    
    for (node, neighbor, distance) in times:
      edges[node-1].append((neighbor-1, distance))
    
    distances = [ 600001 for i in range(n) ]
    distances[start] = 0
    
    visited = set()
    h = []
    heapq.heapify([])
    heapq.heappush(h, (0, start))
    
    while h:
      (dis,node) = heapq.heappop(h)
      distances[node] = dis
      visited.add(node)
      if len(visited) == n:
        break
      for neighbor, distance in edges[node]:
        if neighbor not in visited:
          heapq.heappush(h, (distance + distances[node], neighbor))
        
    m = max(distances)
    return m if m < 600001 else -1
      
      
      