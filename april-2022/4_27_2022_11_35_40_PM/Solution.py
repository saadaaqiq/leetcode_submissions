# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [False for i in range(m)]
        columns = [False for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    columns[j] = True
        
        for i in range(m):
            for j in range(n):
                if rows[i] or columns[j]:
                    matrix[i][j] = 0
                    
                    