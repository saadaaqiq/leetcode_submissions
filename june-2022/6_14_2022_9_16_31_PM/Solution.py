# https://leetcode.com/problems/network-delay-time

class Solution:
  
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
    edges = collections.defaultdict(list)
    for node, neighbor, distance in times:
      edges[node].append((neighbor, distance))
    heap = [(0,k)]    
    visited = set()
    m = 0
    while heap:
      currentDistance, node = heapq.heappop(heap)
      visited.add(node)
      if len(visited) == n:
        return currentDistance
      for neighbor, distance in edges[node]:
        if neighbor not in visited:
          heapq.heappush(heap, (distance + currentDistance, neighbor))
    return -1   
      
      