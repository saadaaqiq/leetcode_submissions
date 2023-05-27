# https://leetcode.com/problems/where-will-the-ball-fall

class Solution:
  def findBall(self, grid: List[List[int]]) -> List[int]:
    m, n = len(grid), len(grid[0])
    balls = [j for j in range(n)]
    
    for arr in grid:
      for j in range(n):
        if balls[j] != -1:
          b = balls[j]
          if arr[b] == 1:
            if (b < n-1 and arr[b+1] == -1) or (b == n-1):
              balls[j] = -1
            else:
              balls[j] += 1
          elif arr[b] == -1:
            if (b > 0 and arr[b-1] == 1) or (b == 0):
              balls[j] = -1
            else:
              balls[j] -= 1
        
    return balls
          