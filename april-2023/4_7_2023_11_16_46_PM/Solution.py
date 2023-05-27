# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dfs(i,j):
            if i == m or j == n:
                return 0
            if s[i] == t[j]:
                return 1 + dfs(i+1,j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))
        
        return dfs(0,0)