# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination

class Solution:
  def shortestPath(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    q = deque([(0,0,0,0)])
    vis = set()
    while q:
      i, j, p, d = q.popleft()
      if p > k or (i,j,p) in vis:
        continue
      if i == m-1 and j == n-1:
        return d
      vis.add((i,j,p))
      for (r,c) in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
        if 0<=r<m and 0<=c<n:
          q.append((r,c,p+grid[r][c],d+1))
    return -1
    