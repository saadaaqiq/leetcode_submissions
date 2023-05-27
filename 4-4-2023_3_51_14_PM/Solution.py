# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n + [1, 1]
        for i in range(n-1, -1, -1):
            dp[i] += dp[i+1] if (0 < int(s[i]) < 10) else 0
            dp[i] += dp[i+2] if (i+1 < n and 0 < int(s[i] + s[i+1]) < 27 and int(s[i]) != 0) else 0
        return dp[0]