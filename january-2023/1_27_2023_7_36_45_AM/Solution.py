# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2,n):
            a, b = b, min(cost[i] + a, cost[i] + b)
        return min(a, b)
