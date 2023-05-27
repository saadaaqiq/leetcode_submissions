# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n-1) + [1 if 1<=int(s[n-1])<=9 else 0, 1, 1]
        for i in range(n-2, -1, -1):
            if 1 <= int(s[i])<= 9:
                dp[i] += dp[i+1]
            if s[i] != "0" and 1 <= int(s[i]+s[i+1]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]
