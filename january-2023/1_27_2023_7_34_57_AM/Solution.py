# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [cost[0], cost[1]] + [0] * (n-1)
        for i in range(2, n+1):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])
        return min(dp[-1], dp[-2])
        