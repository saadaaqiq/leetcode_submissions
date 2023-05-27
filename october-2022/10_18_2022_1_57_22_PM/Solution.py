# https://leetcode.com/problems/minimum-path-sum

class Solution:
  
  def minPathSum(self, grid: List[List[int]]) -> int:
    
    m, n = len(grid), len(grid[0])
    
    dist = [[-1 for j in range(n)] for i in range(m)]
    prev = [[(-1,-1) for j in range(n)] for i in range(m)]
    dist[0][0] = grid[0][0]
    
    heap = [(grid[0][0], 0, 0)]
    heapq.heapify(heap)

    while heap:
      d, i, j = heapq.heappop(heap)
      neighbours = ([(i+1,j)] if i<m-1 else []) + ([(i,j+1)] if j<n-1 else [])
      for r,c in neighbours:
        temp = d + grid[r][c]
        if temp < dist[r][c] or dist[r][c] == -1:
          dist[r][c] = temp
          prev[r][c] = i, j
          heapq.heappush(heap, (temp, r, c))
    
    return dist[m-1][n-1]