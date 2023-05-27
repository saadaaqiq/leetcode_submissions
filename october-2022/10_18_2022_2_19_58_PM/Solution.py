# https://leetcode.com/problems/minimum-path-sum

class Solution:
  
  def minPathSum(self, grid: List[List[int]]) -> int:
    
    # dijkstra solution
    m, n = len(grid), len(grid[0])
    # we put the source in the heap
    heap = [(grid[0][0], 0, 0)]
    # visited set
    visited = set([(0,0)])
    while heap:
      # d: minimum distance from source, guaranteed by the heap
      d, i, j = heapq.heappop(heap)
      # if we find the target we can return the distance 
      if i == m-1 and j == n-1: return d
      # we can only move right or down 
      for r,c in [(i+1, j), (i, j+1)]:
        # we don't want to revisit visited cells
        if r < m and c < n and (r,c) not in visited:
          visited.add((r,c))
          heapq.heappush(heap, (d + grid[r][c], r, c))
    