# https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dfs(i,j):
            if j >= n:
                return i >= m
            if j < n-1 and p[j+1] == "*":
                return dfs(i, j+2) or (i < m and (s[i] == p[j] or p[j] == ".") and dfs(i+1, j))
            return i < m and (s[i] == p[j] or p[j] == ".") and dfs(i+1, j+1)

        return dfs(0, 0)