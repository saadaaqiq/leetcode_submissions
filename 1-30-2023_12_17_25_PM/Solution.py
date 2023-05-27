# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 1
            r = 0
            if 1<= int(s[i]) <= 9:
                r += dfs(i+1)
            if i < n-1 and s[i] != "0" and 1 <= int(s[i]+s[i+1]) <= 26:
                r += dfs(i+2)
            return r

        return dfs(0)        