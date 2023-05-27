# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [-1] * len(cost)

        def dfs(i):
            if i < len(mincost) and mincost[i] >= 0:
                return mincost[i]
            if i >= len(cost):
                return 0
            mincost[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return mincost[i]
        
        dfs(0)
        return min(mincost[0], mincost[1])
        
        
        
        
