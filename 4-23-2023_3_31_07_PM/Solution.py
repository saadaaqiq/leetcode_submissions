# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        mat = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n):
                mat[i][j] = 1+j-i if i>=j else (2+mat[i+1][j-1] if s[i]==s[j] else max(mat[i+1][j], mat[i][j-1]))
        return n - mat[0][n-1]