# https://leetcode.com/problems/number-of-islands

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    
    vis = set()
    cnt = 0
    
    for r in range(m):
      for c in range(n):
        if grid[r][c] == "1" and (r,c) not in vis:
          cnt += 1
          q = deque()
          q.append((r,c))
          while q:
            i,j = q.popleft()
            if (i,j) not in vis:
              vis.add((i,j))
              if i+1<m and grid[i+1][j]=="1":
                q.append((i+1,j))
              if i-1>=0 and grid[i-1][j]=="1":
                q.append((i-1,j))
              if j+1<n and grid[i][j+1]=="1":
                q.append((i,j+1))
              if j-1>=0 and grid[i][j-1]=="1":
                q.append((i,j-1))
    return cnt