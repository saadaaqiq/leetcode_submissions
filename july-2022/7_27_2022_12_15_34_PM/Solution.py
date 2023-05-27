# https://leetcode.com/problems/walls-and-gates

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    q = deque()
    for i in range(len(rooms)):
      for j in range(len(rooms[0])):
        if rooms[i][j] == 0:
          q.append((i,j))
    while q:
      i,j = q.popleft()
      if i+1 < len(rooms) and rooms[i+1][j] == 2147483647:
        q.append((i+1,j))
        rooms[i+1][j] = rooms[i][j] + 1
      if i-1 >= 0 and rooms[i-1][j] == 2147483647:
        q.append((i-1,j))
        rooms[i-1][j] = rooms[i][j] + 1
      if j+1 < len(rooms[0]) and rooms[i][j+1] == 2147483647:
        q.append((i,j+1))
        rooms[i][j+1] = rooms[i][j] + 1
      if j-1 >= 0 and rooms[i][j-1] == 2147483647:
        q.append((i,j-1))
        rooms[i][j-1] = rooms[i][j] + 1
    