# https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [collections.Counter() for _ in range(9)]
        rows = [collections.Counter() for _ in range(9)]
        squares = [collections.Counter() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    rows[i][x] += 1
                    cols[j][x] += 1
                    squares[3 * (i//3) + (j//3)][x] += 1
        for col in cols:
            for k in col:
                if col[k] > 1:
                    return False

        for row in rows:
            for k in row:
                if row[k] > 1:
                    return False
        
        for square in squares:
            for k in square:
                if square[k] > 1:
                    return False
        
        return True