# https://leetcode.com/problems/battleships-in-a-board

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        return sum([(1 if board[i][j] == 'X' and (j==0 or board[i][j-1]=='.') and (i==0 or board[i-1][j]=='.') else 0) for i in range(m) for j in range(n)])