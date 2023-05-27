# https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                matrix[i][j] = matrix[i][j] + min(matrix[i-1][j-1] if j > 0 else float("infinity"), matrix[i-1][j], matrix[i-1][j+1]if j < n - 1 else float("infinity"))
        
        return min(matrix[m-1])