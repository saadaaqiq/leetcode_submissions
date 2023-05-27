# https://leetcode.com/problems/the-maze

class Solution:
  def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    m,n = len(maze), len(maze[0])
    visited = set()
    
    def getNext(r,c):
      
      nextCells = []
      
      i,j=r,c
      while i+1<=m-1 and maze[i+1][c]!=1:
        i+=1
      if (i,c) not in visited:
        nextCells.append((i,c))
        visited.add((i,c))
        
      i,j=r,c
      while i-1>=0 and maze[i-1][c]!=1:
        i-=1
      if (i,c) not in visited:
        nextCells.append((i,c))
        visited.add((i,c))
      
      i,j=r,c
      while j+1<=n-1 and maze[r][j+1]!=1:
        j+=1
      if (r,j) not in visited:
        nextCells.append((r,j))
        visited.add((r,j))
        
      i,j=r,c
      while j-1>=0 and maze[r][j-1]!=1:
        j-=1
      if (r,j) not in visited:
        nextCells.append((r,j))
        visited.add((r,j))
        
      return nextCells
    
    def navigate(i,j):
      print((i,j))
      nexts = getNext(i,j)
      print(nexts)
      print()
      if i==destination[0] and j==destination[1]:
        return True
      for (r,c) in nexts:
        if navigate(r,c):
          return True
      return False
    
    return navigate(start[0],start[1])
