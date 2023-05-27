# https://leetcode.com/problems/surrounded-regions

class Solution:
  
  def solve(self, board: List[List[str]]) -> None:
    
    m, n = len(board), len(board[0])
    
    def dfs(i,j):
      if board[i][j] == 'O':
        board[i][j] = 'T'
        if i+1 < m:
          dfs(i+1,j)
        if i-1 >= 0:
          dfs(i-1,j)
        if j+1 < n:
          dfs(i,j+1)
        if j-1 >= 0: 
          dfs(i,j-1)
          
    for k in range(m):
      if board[k][0] == 'O':
        dfs(k,0)
      if board[k][n-1] == 'O':
        dfs(k,n-1)
    for k in range(n):
      if board[0][k] == 'O':
        dfs(0,k)
      if board[m-1][k] == 'O':
        dfs(m-1,k)
    
    for i in range(m):
      for j in range(n):
        if board[i][j] == 'O':
          board[i][j] = 'X'
        elif board[i][j] == 'T':
          board[i][j] = 'O'
    
    