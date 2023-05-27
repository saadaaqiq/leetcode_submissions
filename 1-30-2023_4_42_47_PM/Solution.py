# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        for x in range(1, amount+1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], 1 + dp[x-c])
        print(dp)
        return dp[-1] if dp[-1] <= amount else -1