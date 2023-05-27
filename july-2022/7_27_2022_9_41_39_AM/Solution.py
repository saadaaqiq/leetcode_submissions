# https://leetcode.com/problems/rotting-oranges

class Solution:
  
  def orangesRotting(self, grid: List[List[int]]) -> int:
    
    m, n = len(grid), len(grid[0])
    
    q = deque()
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 2:
          q.append((i,j,0))
    
    maxi = 0
    while q:
      i,j,c = q.popleft()
      maxi = max(maxi, c)
      if i+1 < m and grid[i+1][j] == 1:
        grid[i+1][j] = 2
        q.append((i+1,j,c+1))
      if j+1 < n and grid[i][j+1] == 1:
        grid[i][j+1] = 2
        q.append((i,j+1,c+1))
      if i-1>= 0 and grid[i-1][j]==1:
        grid[i-1][j] = 2
        q.append((i-1,j,c+1))
      if j-1>= 0 and grid[i][j-1]== 1:
        grid[i][j-1] = 2
        q.append((i,j-1,c+1))
      
      
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          return -1
    
    return maxi
    
    