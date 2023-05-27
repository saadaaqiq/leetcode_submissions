# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        squares = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                x = int(board[i][j])
                if rows[i] & (1<<(x-1)) != 0 or cols[j] & (1<<(x-1)) != 0 or squares[3 * (i//3) + (j//3)] & (1<<(x-1)) != 0:
                    return False
                rows[i] |= (1<<(x-1))
                cols[j] |= (1<<(x-1))
                squares[3 * (i//3) + (j//3)] |= (1<<(x-1))
        return True