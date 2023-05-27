# https://leetcode.com/problems/rotate-image

class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        le = n
        cs, ce, rs, re = 0, n, 0, n
        
        while cs < ce-1 and rs < re-1 and le>1:
            
            for p in range(le-1):

                temp = matrix[rs][cs]

                for c in range(cs+1, ce):
                    k = matrix[rs][c]
                    matrix[rs][c] = temp
                    temp = k

                for r in range(rs+1, re):
                    k = matrix[r][ce-1]
                    matrix[r][ce-1] = temp
                    temp = k

                for c in reversed(range(cs, ce-1)):
                    k = matrix[re-1][c]
                    matrix[re-1][c] = temp
                    temp = k

                for r in reversed(range(rs, re-1)):
                    k = matrix[r][cs]
                    matrix[r][cs] = temp
                    temp = k
        
            le -= 2
            cs += 1
            ce -= 1
            rs += 1
            re -= 1
            
