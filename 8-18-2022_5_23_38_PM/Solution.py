# https://leetcode.com/problems/bomb-enemy

class Solution:
  
  def maxKilledEnemies(self, grid: List[List[str]]) -> int:
    
    m, n = len(grid), len(grid[0])
    maxi = 0
    
    for i in range(m):
      men = 0
      start = 0
      for j in range(n+1):
        if j < n and grid[i][j] == "E":
          men += 1
        if j == n or grid[i][j] == "W":
          for k in range(start, j):
            if grid[i][k] != "E":
              grid[i][k] += men
          start = j + 1
          men = 0
        if j < n and grid[i][j] == "0": 
          grid[i][j] = 0
    
    for j in range(n):
      men = 0
      start = 0
      for i in range(m+1):
        if i < m and grid[i][j] == "E":
          men += 1
        if i == m or grid[i][j] == "W":
          for k in range(start, i):
            if grid[k][j] != "E":
              maxi = max(grid[k][j] + men, maxi)
          start = i + 1
          men = 0
    
    return maxi
            
            
            
            
            
      
        
