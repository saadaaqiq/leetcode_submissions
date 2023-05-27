# https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)] + [0]
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                dp[i] = max(dp[i], dp[i-j]*dp[j])
        return dp[-1]