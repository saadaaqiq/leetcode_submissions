# https://leetcode.com/problems/regular-expression-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dfs(i,j):
            if i >= m and j >= n:
                return True
            if j >= n:
                return False
            b = i < m and (s[i] == p[j] or p[j] == ".")
            if j < n-1 and p[j+1] == "*":
                return dfs(i, j+2) or (b and dfs(i+1, j))
            if b:
                return dfs(i+1, j+1)
            return False

        return dfs(0, 0)