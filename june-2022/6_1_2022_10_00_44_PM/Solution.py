# https://leetcode.com/problems/unique-paths

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    board = [ [ 0 for j in range(n) ] for i in range(m) ]
    visited = set()
    for i in range(m):
      board[i][n-1] = 1
    for j in range(n):
      board[m-1][j] = 1
    q = deque()
    subrow = m-2 if m>=2 else 1
    subcol = n-2 if n>=2 else 1
    q.append((subrow,subcol))
    while q:
      (i,j) = q.popleft()
      if i+1<=m-1 and j+1<=n-1 and board[i+1][j] > 0 and board[i][j+1] > 0:
        board[i][j] = board[i+1][j] + board[i][j+1]
      if j-1>=0 and (i,j-1) not in visited:
        q.append((i,j-1))
        visited.add((i,j-1))
      if i-1>=0 and (i-1,j) not in visited:
        q.append((i-1,j))
        visited.add((i-1,j))
    return board[0][0]