# https://leetcode.com/problems/minimum-path-sum

class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    heap = [(grid[0][0], 0, 0)]
    visited = set([(0,0)])
    while heap:
      d, i, j = heapq.heappop(heap)
      if i == m-1 and j == n-1: return d
      for r,c in [(i+1, j), (i, j+1)]:
        if r < m and c < n and (r,c) not in visited:
          visited.add((r,c))
          temp = d + grid[r][c]
          heapq.heappush(heap, (temp, r, c))
    