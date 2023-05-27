# https://leetcode.com/problems/count-square-submatrices-with-all-ones

class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if mat[i][j] > 0 and mat[i+1][j] > 0 and mat[i][j+1] > 0 and mat[i+1][j+1] > 0:
                    mat[i][j] += min(mat[i+1][j+1], mat[i+1][j], mat[i][j+1])
        return sum([sum(row) for row in mat])