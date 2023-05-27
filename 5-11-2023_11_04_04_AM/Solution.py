# https://leetcode.com/problems/uncrossed-lines

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)

        mat = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    mat[i][j] = 1 + mat[i+1][j+1]
                else:
                    mat[i][j] = max(mat[i+1][j], mat[i][j+1])
        
        return mat[0][0]