# https://leetcode.com/problems/battleships-in-a-board

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        def dfs(i, j):
            board[i][j] = '.'
            for (r,c) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'X':
                    dfs(r, c)
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    res += 1
                    dfs(i, j)
        return res