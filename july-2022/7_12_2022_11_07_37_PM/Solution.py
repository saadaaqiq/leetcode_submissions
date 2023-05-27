# https://leetcode.com/problems/candy-crush

class Solution:
  
  def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
    
    m, n = len(board), len(board[0])

    def checkCell(i,j):
      down,up,left,right = 1,1,1,1
      if board[i][j] != 0:
        while i+down < m and board[i+down][j] == board[i][j]:
          down += 1
        while i-up >= 0 and board[i-up][j] == board[i][j]:
          up += 1
        while j+right <n and board[i][j+right] == board[i][j]:
          right += 1
        while j-left >= 0 and board[i][j-left] == board[i][j]:
          left += 1
      return (down,up,left,right)
    
    def search():
      changed = False
      toBeZeroed = set()
      for i in range(m):
        for j in range(n):
          s = checkCell(i,j)
          if s[0] >= 3:
            for k in range(s[0]):
              toBeZeroed.add((i+k,j))
              changed = True
          if s[1] >= 3:
            for k in range(s[1]):
              toBeZeroed.add((i-k,j))  
              changed = True
          if s[2] >= 3:
            for k in range(s[2]):
              toBeZeroed.add((i,j-k))
              changed = True
          if s[3] >= 3:
            for k in range(s[3]):
              toBeZeroed.add((i,j+k))
              changed = True
      if changed:
        for i,j in toBeZeroed:
          board[i][j] = 0
      return changed
    
    def slideDown():
      for i in range(m):
        for j in range(n):
          if board[i][j] == 0 and (i==m-1 or (board[i+1][j] != 0)):
            k = 0
            while i-k >= 0 and board[i-k][j] == 0:
              k +=1
            for p in range(i, -1, -1):
              if p-k>=0:
                board[p][j] = board[p-k][j]
              else:
                board[p][j] = 0
                
    while search():
      slideDown()
    
    return board
    