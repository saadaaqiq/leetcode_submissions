# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        mat = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    mat[i][j] = 1 + mat[i+1][j+1]
                else:
                    mat[i][j] = max(mat[i][j+1], mat[i+1][j])
        return mat[0][0]