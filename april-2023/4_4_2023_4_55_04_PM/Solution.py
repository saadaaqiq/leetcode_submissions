# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, arr: List[int], n: int) -> int:
        dp = [0] + [inf] * n
        for t in range(n+1):
            for x in arr:
                if t - x >= 0:
                    dp[t] = min(dp[t], 1 + dp[t-x])
        if dp[-1] > n:
            return -1
        return dp[-1] 