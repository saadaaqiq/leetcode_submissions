# https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            for j in range(i-1, 0, -1):
                dp[i] = max(dp[i], max(dp[j],j) * max(i-j, dp[i-j]))
        return dp[-1]