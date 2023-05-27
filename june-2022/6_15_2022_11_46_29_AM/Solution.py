# https://leetcode.com/problems/the-maze-ii

class Solution:
  
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    
    m,n = len(maze), len(maze[0])
    
    def withinLimits(cell):
      i,j = cell
      return True if i>=0 and \
        i<m and j>=0 and j<n and \
        maze[i][j] == 0 \
        else False
    
    visited = set()
    edges = {}
    
    def getNextCells(cell):
      dirs = [(0,1),(1,0),(0,-1),(-1,0)]
      cells = set()
      edges[cell] = []
      for d in dirs:
        c = cell
        dist = 0
        while withinLimits((c[0]+d[0],c[1]+d[1])):
          c = (c[0]+d[0],c[1]+d[1])
          dist += 1
        if dist == 0:
          continue
        cells.add(c)
        edges[cell].append((c, dist))
      return cells
    
    q = deque()
    q.append(tuple(start))
        
    while q:
      cell = q.popleft()
      visited.add(cell)
      nextCells = getNextCells(cell)
      for nextCell in nextCells:
        if nextCell not in visited:
          q.append(nextCell)
    
    print(edges)
    
    size = len(visited)
    visited.clear()
    h = [(0, tuple(start))]
    heapq.heapify(h)
    
    while h:
      distance, cell = heapq.heappop(h)
      visited.add(cell)
      if cell[0] == destination[0] and cell[1] == destination[1]:
        return distance
      if len(visited) == size:
        break
      for nextCell in edges[cell]:
        if nextCell[0] not in visited:
          heapq.heappush(h, (nextCell[1] + distance, nextCell[0]))
    
    return -1
    
    
