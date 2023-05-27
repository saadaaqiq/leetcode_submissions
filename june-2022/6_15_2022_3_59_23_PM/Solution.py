# https://leetcode.com/problems/the-maze-iii

class Solution:
  def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
    
    m, n = len(maze), len(maze[0])
    directions = { (-1,0):'u', (1,0):'d', (0,-1):'l', (0,1):'r' }
    visited = set()
    destination = tuple(hole)
    h = [(0, '.', tuple(ball))]
    heapq.heapify(h)

    minDist, minInst = 1000000, ''
    
    while h:
      
      distance, prev, cell = heapq.heappop(h)
      
      if cell in visited:
        continue  
      visited.add(cell)
      
      if cell == destination:
        minDist, minInst = distance, prev
          
      neighbors = []
      
      for d in directions:
        c = cell
        dist = 0
        while (0 <= c[0]+d[0] < m and 0 <= c[1]+d[1] < n and maze[c[0]+d[0]][c[1]+d[1]] == 0) and \
        ((c[0]+d[0],c[1]+d[1]) != destination):
          c = (c[0] + d[0], c[1] + d[1])
          dist += 1
        if ((c[0]+d[0],c[1]+d[1]) == destination):
          neighbors.append((dist, directions[d], destination))
        else:
          if dist == 0:
            continue
          neighbors.append((dist, directions[d], c))

      for nextCell in neighbors:
        if nextCell[0] not in visited:
          heapq.heappush(h, (nextCell[0] + distance, prev + nextCell[1], nextCell[2]))
    
    return 'impossible' if not minInst else minInst[1:]
    
    