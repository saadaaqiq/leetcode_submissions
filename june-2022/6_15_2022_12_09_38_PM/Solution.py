# https://leetcode.com/problems/the-maze-ii

class Solution:
  
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    
    m,n = len(maze), len(maze[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    h = [(0, tuple(start))]
    heapq.heapify(h)
    visited = set()
    destin = tuple(destination)
    
    while h:
      
      distance, cell = heapq.heappop(h)
      if cell == destin:
        return distance
      visited.add(cell)
      neighbors = []
      
      for d in dirs:
        c = cell
        dist = 0
        while (0 <= c[0]+d[0] < m) and (0 <= c[1]+d[1] < n) and maze[c[0]+d[0]][c[1]+d[1]] == 0:
          c = (c[0]+d[0],c[1]+d[1])
          dist += 1
        if dist == 0:
          continue
        neighbors.append((c, dist))

      for nextCell in neighbors:
        if nextCell[0] not in visited:
          heapq.heappush(h, (nextCell[1] + distance, nextCell[0]))
    
    return -1
    
    
