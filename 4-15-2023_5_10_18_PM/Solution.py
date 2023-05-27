# https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dfs(i, j):
            if i >= m and j >= n:
                return True
            if i >= m and j < n and p[j] == "*":
                return dfs(i, j+1)
            if i >= m and j < n:
                return False
            if i < m and j >= n:
                return False
            return ((s[i] == p[j] or p[j]=="?") and dfs(i+1, j+1)) or (p[j]=="*" and (dfs(i, j+1) or dfs(i+1, j)))
        
        return dfs(0, 0)