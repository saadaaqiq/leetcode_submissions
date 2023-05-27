# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        mat = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mat[i][j] = 1 + mat[i+1][j+1] if s[i]==t[j] else max(mat[i+1][j], mat[i][j+1])

        return mat[0][0]