# https://leetcode.com/problems/valid-sudoku

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    dic = { num : (set(), set(), set()) for num in range(1,10) }
    for i in range(9):
      for j in range(9):
        if board[i][j] != '.':
          num = int(board[i][j])
          if i in dic[num][0] or j in dic[num][1] or (i // 3, j // 3) in dic[num][2]:
            return False
          dic[num][0].add(i)
          dic[num][1].add(j)
          dic[num][2].add((i//3,j//3))
    return True